import pandas as pd
from haversine_alumnos import haversine
import csv

df = pd.read_csv("500_POIs_NY.csv", sep=";")

with open("distancias2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["punto1", "punto2", "distancia"])

    print("Empieza cálculo...")  

    for i in range(len(df)):
        print("Fila:", i)  
        lat1 = df.loc[i, "LATITUDE"]
        lon1 = df.loc[i, "LONGITUDE"]

        for j in range(i + 1, len(df)):
            lat2 = df.loc[j, "LATITUDE"]
            lon2 = df.loc[j, "LONGITUDE"]
            d = haversine(lat1, lon1, lat2, lon2)
            writer.writerow([i, j, d])

    print("Termine")  
