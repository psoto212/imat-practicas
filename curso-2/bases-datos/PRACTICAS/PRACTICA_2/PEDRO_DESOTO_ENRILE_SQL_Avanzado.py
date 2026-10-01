queries = {
    "pregunta1": 
"""
SELECT MAX(t.PRECIO)
FROM billetes b
INNER JOIN trayectos t 
ON t.CODTRAY = b.CODTRAY;

""",

    "pregunta2": 
"""
SELECT CODTRAY
FROM trayectos
ORDER BY PRECIO ASC
LIMIT 1;
""",

    "pregunta3": 
"""
SELECT CBILL
FROM billetes b
INNER JOIN trayectos t
ON b.CODTRAY = t.CODTRAY
WHERE t.PRECIO = (SELECT max(PRECIO) FROM trayectos);


""",

    "pregunta4": 
"""
SELECT CBILL
FROM billetes b
INNER JOIN trayectos t
ON b.CODTRAY = t.CODTRAY
WHERE t.PRECIO > (SELECT AVG(PRECIO) FROM trayectos);

""",

    "pregunta5": 
"""
SELECT UPPER(LEFT(ORIG,4)), UPPER(LEFT(DEST,4))
FROM trayectos
WHERE LENGTH(ORIG)>4 and LENGTH(ORIG)<12;

""",
    "pregunta6": 
"""
SELECT CODTRAY, COUNT(*) AS BILLETES_VENDIDOS
FROM billetes
GROUP BY CODTRAY
HAVING COUNT(*) = (SELECT MAX(vendidos) FROM (SELECT COUNT(*) AS vendidos FROM billetes GROUP BY CODTRAY) x);
""",
    "pregunta7": 
"""
SELECT p.NOMBRE, p.TLFN, b.CODTRAY
FROM pasajeros p
INNER JOIN billetes b
ON b.DNI = p.DNI
GROUP BY p.DNI, b.CODTRAY
HAVING COUNT(*) = (SELECT MAX(v) FROM (SELECT COUNT(*) AS v FROM billetes GROUP BY DNI, CODTRAY) x);

""",
    "pregunta8": 
"""
SELECT b.MATRIC, COUNT(*) AS billetes_vendidos, COUNT(DISTINCT b.DNI) AS pasajeros_llevados
FROM billetes b
INNER JOIN trayectos t 
ON b.CODTRAY = t.CODTRAY
WHERE t.PRECIO = (SELECT MIN(PRECIO) FROM trayectos)
GROUP BY b.MATRIC;


""",
    "pregunta9": 
"""
SELECT p.DNI, p.NOMBRE, COUNT(*) AS num_billetes, COUNT(DISTINCT b.CODTRAY) AS num_trayectos
FROM pasajeros p
INNER JOIN billetes b 
ON b.DNI = p.DNI
WHERE p.TLFN LIKE '63%'
GROUP BY p.DNI, p.NOMBRE;

""",
    "pregunta10": 
"""
SELECT p.*
FROM pasajeros p
INNER JOIN billetes b 
ON b.DNI = p.DNI
GROUP BY p.DNI
HAVING COUNT(*) = (SELECT MAX(v) FROM (SELECT COUNT(*) AS v FROM billetes GROUP BY DNI) x);

""",
    "pregunta11": 
"""
SELECT p.DNI, p.NOMBRE, b.CBILL
FROM pasajeros p
INNER JOIN billetes b 
ON b.DNI = p.DNI
INNER JOIN trayectos t
ON t.CODTRAY = b.CODTRAY
WHERE t.PRECIO = (SELECT MAX(PRECIO) FROM trayectos);

""",
    "pregunta12": 
"""
SELECT b.CBILL, b.CODTRAY, b.MATRIC, a.NASIENTOS
FROM autobuses a
INNER JOIN billetes b 
ON b.MATRIC = a.MATRIC
WHERE a.ITV = '2007-02-05' AND b.FECHA = '2007-02-05';

""",
    "pregunta13": 
"""
SELECT t1.*
FROM trayectos t1
WHERE t1.PRECIO < (SELECT AVG(t2.PRECIO) FROM trayectos t2 WHERE t2.ORIG = t1.ORIG);


""",
    "pregunta14": 
"""
SELECT SUM(t.PRECIO) AS TOTAL_RECAUDADO
FROM billetes b
INNER JOIN trayectos t ON t.CODTRAY = b.CODTRAY;

""",
    "pregunta15": 
"""
SELECT b.CBILL, t.PRECIO
FROM billetes b
INNER JOIN trayectos t 
ON t.CODTRAY = b.CODTRAY
ORDER BY t.PRECIO ASC, b.CBILL DESC;

""",
    "pregunta16": 
"""
SELECT DISTINCT p.NOMBRE, p.TLFN
FROM pasajeros p
INNER JOIN billetes b 
ON b.DNI = p.DNI
INNER JOIN autobuses a 
ON a.MATRIC = b.MATRIC
WHERE b.CODTRAY = 'CT-408' AND b.FECHA = '2007-03-16' AND a.NASIENTOS > 50;

""",
    "pregunta17": 
"""
SELECT t.ORIG, COUNT(*) AS BILLETES_VENDIDOS
FROM trayectos t
INNER JOIN billetes b 
ON b.CODTRAY = t.CODTRAY
WHERE t.PRECIO > 30
GROUP BY t.ORIG;

""",
    "pregunta18": 
"""
SELECT b.CBILL, t.CODTRAY, t.PRECIO
FROM trayectos t
LEFT JOIN billetes b 
ON b.CODTRAY = t.CODTRAY
ORDER BY t.CODTRAY, b.CBILL;

""",
    "pregunta19": 
"""
SELECT a.MATRIC, (a.NASIENTOS - COALESCE(COUNT(b.CBILL),0)) AS ASIENTOS_LIBRES
FROM autobuses a
LEFT JOIN billetes b
  ON b.MATRIC = a.MATRIC
 AND b.CODTRAY = 'CT-XXX'
 AND b.FECHA = '2007-03-16'
 AND b.HORA  = '19:05:21'
GROUP BY a.MATRIC, a.NASIENTOS;
""",
    "pregunta20": 
"""
SELECT c.CODTRAY, c.FECHA
FROM (
  SELECT CODTRAY, FECHA, COUNT(*) AS VENDIDOS
  FROM billetes
  GROUP BY CODTRAY, FECHA
) c
INNER JOIN (
  SELECT CODTRAY, MAX(VENDIDOS) AS MAX_VENDIDOS
  FROM (
    SELECT CODTRAY, FECHA, COUNT(*) AS VENDIDOS
    FROM billetes
    GROUP BY CODTRAY, FECHA
  ) x
  GROUP BY CODTRAY
) m ON m.CODTRAY = c.CODTRAY AND m.MAX_VENDIDOS = c.VENDIDOS;

""",
}

