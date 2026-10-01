import pandas as pd
import numpy as np
import requests
from urllib.parse import urlunsplit, urlencode, urljoin
from bs4 import BeautifulSoup
import io
import re

NORMALIZED_PROVINCES = {
    "Buenos Aires": "Provincia de Buenos Aires",
    "Tucuman": "Tucumán",
    "Entre Rios": "Entre Ríos",
    "Neuquen": "Neuquén",
    "Rio Negro": "Río Negro",
    "Ciudad de Buenos Aires": "Ciudad Autónoma de Buenos Aires",
    "Cordoba": "Córdoba",
}


def get_diputados(url: str) -> pd.DataFrame:
    response = requests.get(url)
    return pd.DataFrame(response.json())


def clean_diputados(diputados: pd.DataFrame) -> pd.DataFrame:
    df = diputados.drop(columns=['periodoMandato', 'periodoBloque', 'juramentoFecha', 'ceseFecha','foto']).copy()
    return df.drop_duplicates()


def normalize_provinces(
    diputados: pd.DataFrame, normalized_provinces: dict
) -> pd.DataFrame:
    df = diputados.copy()
    def cambio(celda):
        if celda in list(normalized_provinces.keys()):
            return normalized_provinces[celda]
        else:
            return celda
    df['provincia'] = df['provincia'].apply(cambio)
    return df


def strip_provinces(diputados: pd.DataFrame) -> pd.DataFrame:
    df = diputados.copy()
    patron = re.compile(r'(?:\s+)?(\w+)(?:\s+)?((?:\s+)?(\w+)(?:\s+)?)?((?:\s+)?(\w+)(?:\s+)?)?((?:\s+)?(\w+)(?:\s+)?)?((?:\s+)?(\w+)(?:\s+)?)?')
    def cambio(celda):
        m = patron.search(celda)
        res = ''
        grupos = m.groups()
        for i in range(0,len(m.groups())):
            if grupos[i] is not None and i in [0,2,4,6,8]:
                res+=grupos[i]
                if i+1< len(m.groups()) and grupos[i+1] is not None:
                    res+=' '
        return res
    df['provincia'] = df['provincia'].apply(cambio)
    return df


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    return soup


def extract_population_table_from_soup(soup: BeautifulSoup) -> pd.DataFrame:
    tabla = soup.find('table',{'class':"wikitable sortable"})
    df = pd.read_html(str(tabla))[0]
    
    df_new = pd.DataFrame()
    df_new['provincia'] = df[1]
    df_new['poblacion'] = df[2]
    return df_new


def population_as_numeric(poblacion: pd.DataFrame) -> pd.DataFrame:
    df = poblacion.copy()
    df=df.drop([0,1,26]) #eliminamos las filas no numericas y total pais
    patron = re.compile(r'(\d+)?(?:\s+)?(\d+)\s+(\d+)')
    def cambio(celda):
        m = patron.search(celda)
        res = ''
        if m.group(1) is not None:
            res += m.group(1)
        return float(res+m.group(2)+m.group(3))
    df['poblacion'] = df['poblacion'].apply(cambio)
    return df.rename(columns={'poblacion':'poblacion_final'})


def diputados_per_province(diputados: pd.DataFrame) -> pd.DataFrame:
    df = diputados.copy()
    new_df = df['provincia'].value_counts().reset_index()
    return new_df.rename(columns={'count':'numero_diputados'})


def diputados_per_inhabitant(
    diputados_por_provincia: pd.DataFrame, poblacion: pd.DataFrame
) -> pd.DataFrame:
    df_dip = diputados_por_provincia.copy()
    df_pob = poblacion.copy()
    df = df_dip.merge(df_pob, on ='provincia')
    df['ratio'] = (df['numero_diputados']/(df['poblacion_final']/100000))
    return df


def plot_histogram(provincias_final: pd.DataFrame) -> None:
    df = provincias_final.copy()
    return df['ratio'].plot(kind='hist')


def plot_boxplot(provincias_final: pd.DataFrame) -> None:
    df = provincias_final.copy()
    return df['ratio'].plot(kind='box')


def find_outliers(provincias_final: pd.DataFrame) -> list:
    df = provincias_final.copy()
    df['zscore']= abs((df['ratio']-df['ratio'].mean())/df['ratio'].std())
    return list(df.loc[df['zscore']>3,'provincia'])
