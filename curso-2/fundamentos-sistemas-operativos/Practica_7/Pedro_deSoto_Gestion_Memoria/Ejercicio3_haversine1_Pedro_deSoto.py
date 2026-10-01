import pandas as pd
from haversine_alumnos import haversine
import csv

df = pd.read_csv("500_POIs_NY.csv", sep=";")

distancias = {}

for i in range(len(df)):
    lat1 = df.loc[i, "LATITUDE"]
    lon1 = df.loc[i, "LONGITUDE"]

    for j in range(len(df)):
        if i != j:
            lat2 = df.loc[j, "LATITUDE"]
            lon2 = df.loc[j, "LONGITUDE"]
            d = haversine(lat1, lon1, lat2, lon2)

            distancias[(i, j)] = d

with open("distancias1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["punto1", "punto2", "distancia"])

    for (i, j), d in distancias.items():
        writer.writerow([i, j, d])
