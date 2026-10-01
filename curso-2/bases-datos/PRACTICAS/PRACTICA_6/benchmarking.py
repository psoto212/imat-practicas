import os
import time
import pymysql
from pymongo import MongoClient
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DATABASE = 'Reviews'
MONGO_URI = os.environ['MONGO_URI']
MONGO_DATABASE = 'Reviews'
MONGO_COLLECTION = 'Videogames'

def get_mysql_connection():
    return pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

def get_mongo_collection():
    client = MongoClient(MONGO_URI)
    collection = client[MONGO_DATABASE][MONGO_COLLECTION]
    return (client, collection)

def Benchmark_1():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = 'SELECT DISTINCT reviewerID FROM Videogames'
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = collection.distinct('reviewerID')
    fin_mongo = time.time()
    print('Benchmark1')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_2():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = 'SELECT reviewerID, AVG(overall), COUNT(*) FROM Videogames GROUP BY reviewerID'
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    pipeline = [{'$group': {'_id': '$reviewerID', 'media_overall': {'$avg': '$overall'}, 'total_reviews': {'$sum': 1}}}]
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = list(collection.aggregate(pipeline))
    fin_mongo = time.time()
    print('Benchmark2')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_3():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = "SELECT * FROM Videogames WHERE LOWER(summary) LIKE '%great%'"
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    filtro_mongo = {'summary': {'$regex': 'great', '$options': 'i'}}
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = list(collection.find(filtro_mongo))
    fin_mongo = time.time()
    print('Benchmark3')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_4():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = 'SELECT asin, AVG(overall) AS media_overall FROM Videogames GROUP BY asin ORDER BY media_overall DESC, asin ASC LIMIT 1'
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    pipeline = [{'$group': {'_id': '$asin', 'media_overall': {'$avg': '$overall'}}}, {'$sort': {'media_overall': -1, '_id': 1}}, {'$limit': 1}]
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = list(collection.aggregate(pipeline))
    fin_mongo = time.time()
    print('Benchmark4')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_5():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = 'SELECT asin, AVG(overall) AS media_overall, COUNT(*) AS total_reviews FROM Videogames GROUP BY asin HAVING COUNT(*) >= 10 ORDER BY media_overall DESC, asin ASC LIMIT 1'
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    pipeline = [{'$group': {'_id': '$asin', 'media_overall': {'$avg': '$overall'}, 'total_reviews': {'$sum': 1}}}, {'$match': {'total_reviews': {'$gte': 10}}}, {'$sort': {'media_overall': -1, '_id': 1}}, {'$limit': 1}]
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = list(collection.aggregate(pipeline))
    fin_mongo = time.time()
    print('Benchmark5')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_6():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = 'SELECT overall, COUNT(*) AS total_reviews FROM Videogames WHERE unixReviewTime >= 1000000000 GROUP BY overall ORDER BY total_reviews ASC'
    inicio_mysql = time.time()
    for _ in range(5):
        cursor.execute(consulta_mysql)
        res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    pipeline = [{'$match': {'unixReviewTime': {'$gte': 1000000000}}}, {'$group': {'_id': '$overall', 'total_reviews': {'$sum': 1}}}, {'$sort': {'total_reviews': 1}}]
    inicio_mongo = time.time()
    for _ in range(5):
        res_mongo = list(collection.aggregate(pipeline))
    fin_mongo = time.time()
    print('Benchmark6')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()

def Benchmark_7():
    conexion_mysql = get_mysql_connection()
    cursor = conexion_mysql.cursor()
    client, collection = get_mongo_collection()
    consulta_mysql = "SELECT * FROM Videogames WHERE LOWER(summary) LIKE '%rpg%' OR LOWER(reviewText) LIKE '%rpg%'"
    inicio_mysql = time.time()
    cursor.execute(consulta_mysql)
    res_mysql = cursor.fetchall()
    fin_mysql = time.time()
    filtro_mongo = {'$or': [{'summary': {'$regex': 'rpg', '$options': 'i'}}, {'reviewText': {'$regex': 'rpg', '$options': 'i'}}]}
    inicio_mongo = time.time()
    res_mongo = list(collection.find(filtro_mongo))
    fin_mongo = time.time()
    print('Benchmark7')
    print('Registros MySQL:', len(res_mysql))
    print('Tiempo MySQL:', fin_mysql - inicio_mysql)
    print('Registros MongoDB:', len(res_mongo))
    print('Tiempo MongoDB:', fin_mongo - inicio_mongo)
    print()
    cursor.close()
    conexion_mysql.close()
    client.close()
if __name__ == '__main__':
    Benchmark_1()
    Benchmark_2()
    Benchmark_3()
    Benchmark_4()
    Benchmark_5()
    Benchmark_6()
    Benchmark_7()
