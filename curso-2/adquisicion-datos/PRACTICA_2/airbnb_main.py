import numpy as np
import pandas as pd
import re


def airbnb_read(archivo):
    """Lee el archivo CSV de Airbnb y devuelve un DataFrame."""
    df = pd.read_csv(archivo)
    return df


def airbnb_size(df):
    """Devuelve el tamaño del DataFrame (filas, columnas)."""
    tamaño = df.shape
    return tamaño


def airbnb_columns(df):
    """Devuelve una lista con los nombres de las columnas del DataFrame."""
    lista_columnas = []
    for i in range(len(df.columns)):
        lista_columnas.append(df.columns[i])
    return lista_columnas


def airbnb_countries(df):
    """Cuenta cuántos registros hay por país (si existe la columna 'country')."""
    if 'country' in df.columns:
        paises = df['country'].value_counts()
        return paises


def airbnb_boroughs(df):
    """Cuenta cuántos registros hay por barrio ('neighbourhood group'),
    corrigiendo posibles errores de escritura."""
    if 'neighbourhood group' in df.columns:
        barrios = df['neighbourhood group'].str.strip().str.title()
        barrios = barrios.replace({'Brookln': 'Brooklyn', 'Manhatan': 'Manhattan'})
        barrios = barrios.value_counts()
        return barrios


def airbnb_price(df):
    """Convierte la columna 'price' a formato numérico y elimina las filas con NaN."""
    if 'price' in df.columns:
        df['price'] = df['price'].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df_nuevo = df.dropna(subset=['price'])
        return df_nuevo


def airbnb_aggregate(df):
    """Calcula media, mediana, mínimo y máximo del precio por barrio."""
    if 'neighbourhood group' in df.columns and 'price' in df.columns:
        resumen = df.groupby('neighbourhood group')['price'].agg(['mean', 'median', 'min', 'max'])
        return resumen


def airbnb_totals(df):
    """Cuenta cuántos alojamientos hay por cada barrio ('neighbourhood group')."""
    totales = df.groupby('neighbourhood group').size().reset_index(name='count')
    totales = totales.sort_values(by='neighbourhood group')
    return totales


def population_totals(df):
    """Agrupa la población total por 'Borough' y la devuelve ordenada."""
    if 'Borough' in df.columns and 'population' in df.columns:
        resumen = df.groupby('Borough')['population'].sum().reset_index(name='population')
        resumen = resumen.sort_values(by='Borough')
        return resumen


def airbnb_population(df_airbnb, df_population):
    """Une los datos de Airbnb y población para calcular el número de Airbnbs
    por cada 1000 habitantes en cada Borough."""
    df_merged = pd.merge(df_airbnb, df_population, left_on='neighbourhood group', right_on='Borough')
    df_merged['airbnbs_per_thousands'] = (df_merged['count'] / df_merged['population']) * 1000
    return df_merged[['Borough', 'airbnbs_per_thousands']]



if __name__ == "__main__":
    archivo = input("Escriba el nombre del archivo de Airbnb (.csv): ")

    if archivo.endswith('.csv'):
        df = airbnb_read(archivo)

        print("\nTamaño del DataFrame:")
        print(airbnb_size(df))

        print("\nColumnas:")
        print(airbnb_columns(df))

        print("\nPaíses:")
        print(airbnb_countries(df))

        print("\nBarrios:")
        print(airbnb_boroughs(df))

        print("\nLimpieza de precios:")
        df = airbnb_price(df)
        print(df.head())

        print("\nEstadísticas por barrio:")
        print(airbnb_aggregate(df))

        print("\nTotales de Airbnbs por barrio:")
        df_airbnb_totals = airbnb_totals(df)
        print(df_airbnb_totals)

        # Leer el archivo de población
        df_population = pd.read_csv('population.csv')

        print("\nTotales de población por Borough:")
        df_population_totals = population_totals(df_population)
        print(df_population_totals)

        print("\nAirbnbs por cada 1000 habitantes:")
        df_airbnb_population = airbnb_population(df_airbnb_totals, df_population_totals)
        print(df_airbnb_population)
