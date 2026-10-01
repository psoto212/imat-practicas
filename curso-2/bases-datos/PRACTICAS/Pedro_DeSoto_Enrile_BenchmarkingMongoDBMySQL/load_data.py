import os
import pymysql
import json
from pymongo import MongoClient
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DATABASE = 'Reviews'
MONGO_URI = os.environ['MONGO_URI']
MONGO_DATABASE = 'Reviews'
MONGO_COLLECTION = 'Videogames'

def inserta_mongodb(json_file_path):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    collection = db[MONGO_COLLECTION]
    collection.delete_many({})
    docs = []
    with open(json_file_path, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                docs.append(json.loads(linea))
                if len(docs) == 1000:
                    collection.insert_many(docs)
                    docs = []
        if docs:
            collection.insert_many(docs)
    client.close()

def inserta_datos_mysql(json_file_path):
    conexion_inicial = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD)
    cursor_inicial = conexion_inicial.cursor()
    cursor_inicial.execute('CREATE DATABASE IF NOT EXISTS Reviews')
    conexion_inicial.commit()
    cursor_inicial.close()
    conexion_inicial.close()
    conexion = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
    cursor = conexion.cursor()
    cursor.execute('DROP TABLE IF EXISTS Videogames')
    cursor.execute('\n        CREATE TABLE Videogames (\n            reviewerID VARCHAR(100),\n            asin VARCHAR(30),\n            reviewerName TEXT,\n            helpful_1 INT,\n            helpful_2 INT,\n            reviewText TEXT,\n            overall FLOAT,\n            summary TEXT,\n            unixReviewTime BIGINT,\n            reviewTime VARCHAR(50)\n        )\n    ')
    with open(json_file_path, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                doc = json.loads(linea)
                helpful = doc.get('helpful', [None, None])
                cursor.execute('\n                    INSERT INTO Videogames\n                    (reviewerID, asin, reviewerName, helpful_1, helpful_2,\n                     reviewText, overall, summary, unixReviewTime, reviewTime)\n                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)\n                ', (doc.get('reviewerID'), doc.get('asin'), doc.get('reviewerName'), helpful[0] if len(helpful) > 0 else None, helpful[1] if len(helpful) > 1 else None, doc.get('reviewText'), doc.get('overall'), doc.get('summary'), doc.get('unixReviewTime'), doc.get('reviewTime')))
    conexion.commit()
    cursor.close()
    conexion.close()
if __name__ == '__main__':
    inserta_mongodb('Video_Games_5.json')
    inserta_datos_mysql('Video_Games_5.json')
    print('Datos cargados en MongoDB y MySQL')
