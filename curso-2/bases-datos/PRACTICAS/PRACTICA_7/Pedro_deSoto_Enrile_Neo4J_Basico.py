queries = {
    "pregunta1": """
MATCH (p:Movie)
WHERE p.released = 2006
RETURN p.title
""",

    "pregunta2": """
MATCH (persona:Person)-[:DIRECTED]->(pelicula:Movie)
WHERE pelicula.released = 2006
RETURN persona, pelicula
""",

    "pregunta3": """
MATCH (p:Person {name:'Clint Eastwood'})-[r]->(pelicula:Movie)
RETURN pelicula.title, TYPE(r)
""",

    "pregunta4": """
MATCH (p:Person {name:'Keanu Reeves'})-[r:ACTED_IN]->(pelicula:Movie)
UNWIND r.roles AS personaje
RETURN pelicula.title, personaje
""",

    "pregunta5": """
MATCH (persona:Person)-[r:REVIEWED]->(pelicula:Movie)
WHERE TOLOWER(r.summary) CONTAINS 'but'
RETURN persona.name, pelicula.title, r.rating, r.summary
""",

    "pregunta6": """
MATCH (persona:Person)-[:DIRECTED]->(dirigida:Movie)
MATCH (persona)-[:ACTED_IN]->(actuada:Movie)
WHERE dirigida <> actuada
RETURN persona, actuada
""",

    "pregunta7": """
MATCH (persona:Person)-[:PRODUCED]->(pelicula:Movie)
WHERE NOT (persona)-[:DIRECTED]->(pelicula)
  AND NOT (persona)-[:ACTED_IN]->(pelicula)
RETURN persona, pelicula
""",

    "pregunta8": """
MATCH (actor:Person)-[:ACTED_IN]->(pelicula:Movie)<-[:DIRECTED]-(director:Person)
WHERE actor = director
RETURN actor.name, director.name, pelicula.title
""",

    "pregunta9": """
MATCH (pelicula:Movie)
WHERE pelicula.released IN [2000, 2004, 2008]
RETURN pelicula.title, pelicula.released
""",

    "pregunta10": """
MATCH (persona:Person)-[:REVIEWED]->(pelicula:Movie)<-[:DIRECTED]-(director:Person)
RETURN persona, pelicula, director
""",

    "pregunta11": """
MATCH (actor1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(actor2:Person)
MATCH (actor2)-[:DIRECTED]->(otra:Movie)<-[:ACTED_IN]-(actor1)
WHERE m <> otra AND actor1 <> actor2
RETURN actor1, actor2, m, otra
""",

    "pregunta12": """
MATCH (:Person {name:'Keanu Reeves'})-[:ACTED_IN]->(pelicula:Movie)
MATCH (director:Person)-[:DIRECTED]->(pelicula)
MATCH (actor:Person)-[:ACTED_IN]->(pelicula)
RETURN pelicula.title, director.name, COLLECT(DISTINCT actor.name) AS actores
""",

    "pregunta13": """
MATCH (p:Person {name:'Charlize Theron'})-[:ACTED_IN]->(pelicula:Movie)
WITH pelicula, date().year - pelicula.released AS anios_desde_estreno, pelicula.released - p.born AS edad_charlize
RETURN pelicula.title, pelicula.released, anios_desde_estreno, edad_charlize
ORDER BY anios_desde_estreno
""",

    "pregunta14": """
MATCH (actor:Person)-[:ACTED_IN]->(pelicula:Movie)
WITH actor, COUNT(pelicula) AS num_peliculas
WHERE num_peliculas >= 5
RETURN actor.name, num_peliculas
""",

    "pregunta15": """
MATCH (persona:Person)-[r:REVIEWED]->(pelicula:Movie)
MATCH (actor:Person)-[:ACTED_IN]->(pelicula)
RETURN persona.name, pelicula.title, pelicula.released, r.rating, COLLECT(DISTINCT actor.name) AS actores
""",

    "pregunta16": """
MATCH (director:Person)-[:DIRECTED]->(pelicula:Movie)
OPTIONAL MATCH (actor:Person)-[:ACTED_IN]->(pelicula)
RETURN director.name, COLLECT(DISTINCT actor.name) AS actores
ORDER BY director.name
""",

    "pregunta17": """
MATCH (director:Person)-[:DIRECTED]->(pelicula:Movie)<-[:REVIEWED]-(persona:Person)
WHERE (persona)<-[:FOLLOWS]-(:Person)
RETURN pelicula, director, persona
""",

    "pregunta18": """
MATCH (director:Person)-[:DIRECTED]->(pelicula:Movie)
WITH director, COUNT(DISTINCT pelicula) AS total
WHERE total > 2
MATCH (director)-[:DIRECTED]->(pelicula:Movie)
OPTIONAL MATCH (actor:Person)-[:ACTED_IN]->(pelicula)
RETURN pelicula, director, actor
""",

    "pregunta19": """
MATCH (:Person {name:'John Cusack'})-[r:ACTED_IN]->(:Movie {title:'Stand By Me'})
SET r.roles = ['D. Lachance']
RETURN r
""",

    "pregunta20": """
CREATE (yo:Person {name:'TU_NOMBRE'})
WITH yo
MATCH (pelicula:Movie {title:'The Matrix'})
CREATE (yo)-[:REVIEWED {rating:100, summary:'Excelente pelicula'}]->(pelicula)
RETURN yo, pelicula
"""
}