import pymysql
from datetime import datetime

MYSQL_CONFIG = {
    "host": "127.0.0.1",
    "user": "pedrosoto",
    "password": "pse@2005",
    "port": 3306,
    "database": "Lastfm",
    "charset": "utf8mb4",
}

PATH_PROFILE = r"C:\Users\psoto\OneDrive - Universidad Pontificia Comillas\2º de iMat\2o cuatri\BASES\PRACTICAS\PRACTICA_3\userid-profile.tsv"
PATH_LISTENS = r"C:\Users\psoto\OneDrive - Universidad Pontificia Comillas\2º de iMat\2o cuatri\BASES\PRACTICAS\PRACTICA_3\userid-timestamp-artid-artname-traid-traname.tsv"
BATCH_SIZE = 5000
MAX_LISTENS = 1_000_000


DDL = [
    "CREATE DATABASE IF NOT EXISTS Lastfm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
    "USE Lastfm",
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT NOT NULL AUTO_INCREMENT,
        userid VARCHAR(64) NOT NULL,
        genero VARCHAR(16) NULL,
        edad INT NULL,
        pais VARCHAR(128) NULL,
        signup DATE NULL,
        PRIMARY KEY (id_usuario),
        UNIQUE KEY uk_usuarios_userid (userid)
    ) ENGINE=InnoDB
    """,
    """
    CREATE TABLE IF NOT EXISTS artistas (
        id_artista INT NOT NULL AUTO_INCREMENT,
        artid VARCHAR(250) NULL,
        nombre_artista VARCHAR(250) NULL,
        PRIMARY KEY (id_artista),
        UNIQUE KEY uk_artistas_artid (artid)
    ) ENGINE=InnoDB
    """,
    """
    CREATE TABLE IF NOT EXISTS canciones (
        id_cancion INT NOT NULL AUTO_INCREMENT,
        traid VARCHAR(250) NOT NULL,
        nombre_cancion VARCHAR(250) NULL,
        id_artista INT NULL,
        PRIMARY KEY (id_cancion),
        UNIQUE KEY uk_canciones_traid (traid),
        KEY idx_canciones_artista (id_artista),
        CONSTRAINT fk_canciones_artistas
            FOREIGN KEY (id_artista) REFERENCES artistas(id_artista)
            ON UPDATE CASCADE
            ON DELETE SET NULL
    ) ENGINE=InnoDB
    """,
    """
    CREATE TABLE IF NOT EXISTS escuchas (
        id_escucha BIGINT NOT NULL AUTO_INCREMENT,
        id_usuario INT NOT NULL,
        id_cancion INT NOT NULL,
        fecha_escucha DATETIME NOT NULL,
        PRIMARY KEY (id_escucha),
        KEY idx_escuchas_usuario (id_usuario),
        KEY idx_escuchas_cancion (id_cancion),
        KEY idx_escuchas_fecha (fecha_escucha),
        CONSTRAINT fk_escuchas_usuarios
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
        CONSTRAINT fk_escuchas_canciones
            FOREIGN KEY (id_cancion) REFERENCES canciones(id_cancion)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
    ) ENGINE=InnoDB
    """,
]


def connect_mysql_no_db():
    tmp_cfg = dict(MYSQL_CONFIG)
    tmp_cfg.pop("database", None)
    return pymysql.connect(**tmp_cfg, autocommit=False)


def ensure_db_and_tables(cur):
    for stmt in DDL:
        cur.execute(stmt)


def parse_signup(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%b %d, %Y").date()
    except ValueError:
        return None


def parse_listen_time(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None


def load_users(cur):
    user_map = {}

    insert_sql = """
        INSERT INTO usuarios (userid, genero, edad, pais, signup)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            genero = COALESCE(VALUES(genero), genero),
            edad = COALESCE(VALUES(edad), edad),
            pais = COALESCE(VALUES(pais), pais),
            signup = COALESCE(VALUES(signup), signup)
    """

    batch = []

    with open(PATH_PROFILE, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip("\r\n")
            if not line:
                continue
            parts = line.split("\t")
            while len(parts) < 5:
                parts.append("")
            uid, gender, age, country, signup = parts[0], parts[1], parts[2], parts[3], parts[4]

            uid = (uid or "").strip()
            if not uid:
                continue

            gender = (gender or "").strip() or None
            country = (country or "").strip() or None

            try:
                age_val = int(age) if (age or "").strip() else None
            except ValueError:
                age_val = None

            signup_date = parse_signup(signup)

            batch.append((uid, gender, age_val, country, signup_date))

            if len(batch) >= BATCH_SIZE:
                cur.executemany(insert_sql, batch)
                batch.clear()

    if batch:
        cur.executemany(insert_sql, batch)

    cur.execute("SELECT userid, id_usuario FROM usuarios")
    for uid, idu in cur.fetchall():
        user_map[str(uid)] = int(idu)

    return user_map


def get_or_create_user(cur, user_map, userid):
    userid = (userid or "").strip()
    if not userid:
        raise ValueError("userid vacío")

    if userid in user_map:
        return user_map[userid]

    cur.execute(
        "INSERT INTO usuarios (userid, genero, edad, pais, signup) VALUES (%s, NULL, NULL, NULL, NULL)",
        (userid,),
    )
    new_id = cur.lastrowid
    user_map[userid] = int(new_id)
    return int(new_id)


def get_or_create_artist(cur, artist_map, artid, artname):
    artid = (artid or "").strip()
    if not artid:
        return None

    if artid in artist_map:
        return artist_map[artid]

    cur.execute(
        "INSERT IGNORE INTO artistas (artid, nombre_artista) VALUES (%s, %s)",
        (artid, (artname or "").strip() or None),
    )

    if cur.lastrowid:
        aid = int(cur.lastrowid)
    else:
        cur.execute("SELECT id_artista FROM artistas WHERE artid = %s", (artid,))
        row = cur.fetchone()
        aid = int(row[0]) if row else None

    if aid is not None:
        artist_map[artid] = aid
    return aid


def get_or_create_track(cur, track_map, traid, traname, id_artista):
    traid = (traid or "").strip()
    if not traid:
        raise ValueError("traid vacío (filtra antes)")

    if traid in track_map:
        return track_map[traid]

    cur.execute(
        "INSERT IGNORE INTO canciones (traid, nombre_cancion, id_artista) VALUES (%s, %s, %s)",
        (traid, (traname or "").strip() or None, id_artista),
    )

    if cur.lastrowid:
        tid = int(cur.lastrowid)
    else:
        cur.execute("SELECT id_cancion FROM canciones WHERE traid = %s", (traid,))
        row = cur.fetchone()
        tid = int(row[0])

    track_map[traid] = tid
    return tid


def load_listens(cur, user_map):
    artist_map = {}
    track_map = {}

    insert_listen = "INSERT INTO escuchas (id_usuario, id_cancion, fecha_escucha) VALUES (%s, %s, %s)"

    batch = []
    inserted = 0

    with open(PATH_LISTENS, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if inserted >= MAX_LISTENS:
                break
            line = line.strip("\r\n")
            if not line:
                continue
            parts = line.split("\t")
            while len(parts) < 6:
                parts.append("")
            userid, ts, artid, artname, traid, traname = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]

            traid = (traid or "").strip()
            if not traid:
                continue

            listened_at = parse_listen_time(ts)
            if listened_at is None:
                continue

            id_usuario = get_or_create_user(cur, user_map, userid)
            id_artista = get_or_create_artist(cur, artist_map, artid, artname)
            id_cancion = get_or_create_track(cur, track_map, traid, traname, id_artista)

            batch.append((id_usuario, id_cancion, listened_at))
            inserted += 1

            if len(batch) >= BATCH_SIZE:
                cur.executemany(insert_listen, batch)
                batch.clear()

    if batch:
        cur.executemany(insert_listen, batch)

    return inserted


def main():
    cnx = connect_mysql_no_db()
    try:
        cur = cnx.cursor()
        ensure_db_and_tables(cur)
        cnx.commit()
        cur.close()
    except Exception:
        cnx.rollback()
        raise
    finally:
        cnx.close()

    cnx2 = pymysql.connect(**MYSQL_CONFIG, autocommit=False)
    try:
        cur2 = cnx2.cursor()
        cur2.execute("USE Lastfm")

        user_map = load_users(cur2)
        cnx2.commit()

        n = load_listens(cur2, user_map)
        cnx2.commit()

        print("Usuarios:", len(user_map))
        print("Escuchas insertadas:", n)
    except Exception:
        cnx2.rollback()
        raise
    finally:
        try:
            cur2.close()
        except Exception:
            pass
        cnx2.close()


if __name__ == "__main__":
    main()
