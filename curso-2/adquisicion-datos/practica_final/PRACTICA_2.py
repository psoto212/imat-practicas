import pandas as pd
import numpy as np


"""
ejercicio 1 
Una función airbnb_read que tome como argumento el path al archivo airbnb.csv,
lea el contenido y devuelva el mismo en formato DataFrame.

"""

def airbnb_read(csv):
    df = pd.read_csv(csv)

    return df


"""
ejercicio 2 
Una función airbnb_size que tome como argumento un DataFrame y devuelva sus
dimensiones en formato (n_filas, n_columnas).
"""

def airbnb_size(df):
    tamaño = df.shape

    return tamaño

"""
Ejercicio 3
Una función airbnb_columns que tome como argumento un DataFrame y devuelva
una lista con los nombres de las columnas, en el orden original.

"""

def airbnb_columns(df):
    columnas = df.columns
    return columnas

"""
ejercicio 4
Una función airbnb_countries que tome como argumento el DataFrame inicial y
devuelva un objeto Series. El índice deberá ser el nombre de cada país en el dataset
y el valor corresponderá al número de alojamientos que hay en ese país.

"""

def airbnb_countries(df):
    paises = df['country'].value_counts()

    return paises




