queries = {
    "pregunta1": """
db.peliculasCuestionario.find({}, { _id: 0, pais: 0, actores: 0, genero: 0 })

""",

    "pregunta2": """
db.peliculasCuestionario.find( {pais:{$in:["USA"]}}, {titulo :1, director:1, duracion:1, puntuacion:1})

""",

    "pregunta3": """
db.peliculasCuestionario.find( {pais:{$in:["USA"]}}, {titulo :1, director:1, duracion:1, puntuacion:1}).limit(4)
""",

    "pregunta4": """
db.peliculasCuestionario.find({}, {titulo:1, actores:1, genero:1, puntuacion:1}).sort({puntuacion:-1})
""",

    "pregunta5": """
db.peliculasCuestionario.find({}, {titulo:1, actores:1, genero:1, puntuacion:1}).sort({puntuacion:-1}).limit(1)
""",

    "pregunta6": """
db.peliculasCuestionario.find({$or:[{año:{$gt:2015}}, {puntuacion:{$gt:8}}]}, {_id:0,titulo:1, año:1, puntuacion:1}).sort({año:1, puntuacion:1})
""",

    "pregunta7": """
db.peliculasCuestionario.find({$and:[{año:{$gte:1970}}, {año:{$lte:2000}}]}).sort({año:1})
""",

    "pregunta8": """
db.peliculasCuestionario.find({$and:[{duracion:{$lt:150}}, {puntuacion:{$gte:8}}]}).sort({puntuacion:-1})
""",

    "pregunta9": """
db.peliculasCuestionario.find({director:{$in:["George Lucas", "Quentin Tarantino", "Peter Jackson"]}}, {titulo :1, director:1, año:1, actores:1})
""",

    "pregunta10": """
db.peliculasCuestionario.find({"actores.0":{$in:["Brad Pitt","Johnny Depp"]}}).sort({duracion:-1})
""",

    "pregunta11": """
db.peliculasCuestionario.find({secuela:{$exists:true},año:{$gt:2010}}).sort({año:1})
""",

    "pregunta12": """
db.peliculasCuestionario.find( {actores:{$in:["Harrison Ford"]}}, {titulo :1, director:1, actores:1})
""",

    "pregunta13": """
db.peliculasCuestionario.updateMany({director:"Peter Jackson"}, {$set:{director:"Jackson, Peter"}})
""",

    "pregunta14": """
db.peliculasCuestionario.updateMany({pais:"USA"}, {$set:{pais:"EEUU"}})
""",

    "pregunta15": """
db.peliculasCuestionario.bulkWrite([{updateOne:{filter:{titulo:"8 apellidos vascos"},update:{$set:{secuela:"8 apellidos catalanes",puntuacion:7}}}},{deleteOne:{filter:{puntuacion:{$lte:5.5}}}},{replaceOne:{filter:{titulo:"El club de la lucha"},replacement:{titulo:"El club de los poetas muertos",pais:"EE. UU.",año:1989,genero:"drama",duracion:128,presupuesto:16.4,recaudacion:235.86,puntuacion:7.6,actores:["Robin Williams","Robert Sean Leonard"]}}}])
""",

    "pregunta16": """
db.peliculasCuestionario.find({puntuacion:{$gt:7}}); db.peliculasCuestionario.find({puntuacion:{$gt:7}}).explain("executionStats"); db.peliculasCuestionario.createIndex({puntuacion:-1}); db.peliculasCuestionario.find({puntuacion:{$gt:7}}).explain("executionStats")
""",

    "pregunta17": """
db.peliculasCuestionario.find({presupuesto:{$gt:100}}); db.peliculasCuestionario.find({presupuesto:{$gt:100}}).explain("executionStats"); db.peliculasCuestionario.createIndex({presupuesto:1}); db.peliculasCuestionario.find({presupuesto:{$gt:100}}).explain("executionStats")
""",

    "pregunta18": """
db.peliculasCuestionario.createIndex({genero:"text"}); db.peliculasCuestionario.find({$text:{$search:"accion comedia"}},{_id:0,titulo:1,genero:1,score:{$meta:"textScore"}}).sort({score:{$meta:"textScore"}})
""",

    "pregunta19": """
db.peliculasCuestionario.aggregate([{$group:{_id:"$clasificacion",totalRecaudado:{$sum:"$recaudacion"},mediaDuracion:{$avg:"$duracion"},menorPuntuacion:{$min:"$puntuacion"},mayorPresupuesto:{$max:"$presupuesto"}}},{$sort:{mediaDuracion:1}}])
""",

    "pregunta20": """
db.peliculasCuestionario.aggregate([{$group:{_id:"$pais",sumaPresupuestos:{$sum:"$presupuesto"},sumaRecaudaciones:{$sum:"$recaudacion"},mediaPuntuaciones:{$avg:"$puntuacion"},ultimoAño:{$max:"$año"},duracionMinima:{$min:"$duracion"}}},{$sort:{ultimoAño:1}}])
""",

    "pregunta21": """
db.peliculasCuestionario.aggregate([{$match:{$or:[{productora:"Marvel Studios"},{puntuacion:{$gt:7}}]}},{$group:{_id:"$productora",añoMasAntiguo:{$min:"$año"},presupuestoMedio:{$avg:"$presupuesto"},puntuacionMedia:{$avg:"$puntuacion"}}}])
""",

    "pregunta22": """
db.peliculasCuestionario.aggregate([{$match:{$or:[{presupuesto:{$lt:100}},{puntuacion:{$gt:8}}]}},{$group:{_id:"$clasificacion",recaudacionMedia:{$avg:"$recaudacion"},mayorPresupuesto:{$max:"$presupuesto"},peorPuntuacion:{$min:"$puntuacion"},puntuacionMedia:{$avg:"$puntuacion"}}}])
"""
}