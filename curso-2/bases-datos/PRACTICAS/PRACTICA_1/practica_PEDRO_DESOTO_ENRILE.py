queries = {
    "pregunta1": 
"""
SELECT ORIG, DEST, KM
FROM trayectos
WHERE KM > 150
ORDER BY KM ASC;

""",

    "pregunta2": 
"""
SELECT DISTINCT PRECIO
FROM trayectos
ORDER BY PRECIO DESC;

""",

    "pregunta3": 
"""
SELECT MATRIC, CBILL, FECHA, HORA
FROM billetes
ORDER BY MATRIC DESC, CBILL DESC, FECHA ASC, HORA ASC;

""",

    "pregunta4": 
"""
SELECT CBILL, FECHA, HORA
FROM billetes
WHERE MATRIC = '1234GKH'
  AND FECHA BETWEEN '2007-01-02' AND '2017-12-31'
ORDER BY CBILL ASC;

""",

    "pregunta5": 
"""
SELECT *
FROM pasajeros
ORDER BY NOMBRE ASC;

""",
    "pregunta6": 
"""
SELECT CODTRAY
FROM trayectos
WHERE CODTRAY NOT IN (
    SELECT CODTRAY
    FROM billetes
);

""",
    "pregunta7": 
"""
SELECT a.MATRIC, b.CBILL
FROM autobuses a
INNER JOIN billetes b
ON a.MATRIC = b.MATRIC
WHERE a.ITV = '2007-02-05'
  AND b.FECHA = '2007-02-05';

""",
    "pregunta8": 
"""
SELECT p.NOMBRE
FROM billetes b
INNER JOIN pasajeros p
ON b.DNI = p.DNI
WHERE b.FECHA BETWEEN '2017-11-11' AND '2017-12-03'
  AND b.HORA = '09:00';

""",
    "pregunta9": 
"""
SELECT CODTRAY
FROM trayectos
ORDER BY KM DESC
LIMIT 1;

""",
    "pregunta10": 
"""
SELECT p.DNI, b.CBILL
FROM pasajeros p
INNER JOIN billetes b
ON p.DNI = b.DNI
WHERE p.NOMBRE LIKE '%PEREZ%';

""",
    "pregunta11": 
"""
SELECT *
FROM trayectos t
WHERE t.CODTRAY = 'CT-403'
  AND EXISTS (
      SELECT 1
      FROM billetes b
      WHERE b.CODTRAY = t.CODTRAY
  );

""",
    "pregunta12": 
"""

SELECT *
FROM trayectos
WHERE CODTRAY = 'CT-403'
  AND EXISTS (
      SELECT 1
      FROM billetes
      WHERE CODTRAY = 'CT-405'
  );

""",
    "pregunta13": 
"""

SELECT NOMBRE, b.DNI
FROM billetes b
INNER JOIN pasajeros p
ON b.DNI = p.DNI
WHERE FECHA != '2007-03-16' AND MATRIC = '5482FDH';


""",
    "pregunta14": 
"""
SELECT COUNT(*) AS total_billetes
FROM billetes;

""",
    "pregunta15": 
"""

SELECT AVG(PRECIO) AS media, MAX(PRECIO) AS mas_caro, MIN(PRECIO) AS mas_barato
FROM trayectos;

""",
}

