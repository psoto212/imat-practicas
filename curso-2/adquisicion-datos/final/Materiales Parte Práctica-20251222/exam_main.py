import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re

MONSTERS_SELECTED = ['aarakocra', 'basilisk', 'gorgon', 'mind-flayer', 'yuan-ti-abomination']


# 1
# 1.a
def get_soup(url: str) -> BeautifulSoup:
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup
# 1.b
def generate_database(soup: BeautifulSoup) -> pd.DataFrame:
    table = requests.find('table', class_ = "name")
    df = pd.read_html(str(table))[0]
    df = df[["Creature", "Type", "Alignment"]]
    return df

# 1.c
def make_uniform_name(monsters_df_1c: pd.DataFrame) -> pd.DataFrame:
    df = monsters_df_1c.copy()
    df["Creatures"] = df["Creatures"].str.replace(" ", "-")
    df["Creatures"] = df["Creatures"].lower()
    return df

# 1.d
def get_second_type(monsters_df_1d: pd.DataFrame) -> pd.DataFrame:
    df = monsters_df_1d.copy()
    df["Type"] = df["Type"].re.compile(r"()")
    pass



# 2
def get_api_database(monsters_selected: list[str]) -> pd.DataFrame:
    pass


    

# 3
# 3.a
def join_sources(monsters_df_3_web: pd.DataFrame, 
                 monsters_df_3_api: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(monsters_df_3_web, monsters_df_3_api, on="Creature", how="left")
    df = df[["Creature", "Type", "Second Type", "Alignment", "Strength", "Wisdom" , "Charisma"]]
    return df

    

# 3.b
def impute_missing(monsters_df_3b: pd.DataFrame) -> pd.DataFrame:
    df = monsters_df_3b.copy()
    medianas = df.groupby("Alignment")["Strength"].transform("median")
    df["Strength"] = df["Strenth"].fillna(medianas)
    return df


# 3.c
def delete_outliers(monsters_df_3c: pd.DataFrame) -> tuple[pd.DataFrame]:
    df = monsters_df_3c.copy()
    q1 = df["Strength"].quantile(0.25)
    q3 = df["Strength"].quantile(0.75)

    iqr = q3 - q1
    lim_inf = df["Strength"] - 2.5*iqr
    lim_sup = df["Strength"] + 2.5*iqr

    anomalos = df[(df["Strength"] < lim_inf) | (df["Strength"] > lim_sup)]


    for anomalo in anomalos:
        df.drop(anomalo)
        df_anomalos = pd.DataFrame(anomalo)
        return df_anomalos
    
    return df


# 3.d
# Deja tu respuesta aquí
# porque la varianza de los datos es mayor que la estandar por tanto si 
# dejamos el multiplicador en 1.5 perderiamos muchos datos
# la mediana la hemos usado porque es el dato mas comun





