import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import json
import time
from io import StringIO
from scipy import stats


MESES = {
    "January": "ENE", "February": "FEB", "March":  "MAR", "April":   "ABR",
    "May":     "MAY", "June":     "JUN", "July":   "JUL", "August":  "AGO",
    "September": "SEP", "October": "OCT", "November": "NOV", "December": "DIC"
}

NEW_COLUMNS_1C = ['Title', 'Details', 'US [1]', 'US Latin [2]', 'BEL (WA) [3]', 'CAN [4]', 'FRA [5]',
                  'ITA [6]', 'NLD [7]', 'SPA [8]','SWI [9]', 'UK [10]', 'Sales[A]', 
                  'Certifications', 'Unnamed: 14_level_1']

ID_ARTIST_BAD_BUNNY = "10583405"

# 1. EJERCICIO 1: WEB SCRAPING
# 1.a
def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url, headers={"User-Agent": "AcquisicionDatos/1.0 (estudiante@universidad.es)"})
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
# 1.b
def obtain_albums(soup: BeautifulSoup) -> pd.DataFrame:
    tabla = soup.find("table", class_="wikitable plainrowheaders")

    df = pd.read_html(str(tabla))[0]

    return df

# 1.c
def clean_albums(albums: pd.DataFrame) -> pd.DataFrame:
    albums = albums[:6]
    return albums

# 1.d
def extract_dates_sales(albums_cleaned: pd.DataFrame) -> pd.DataFrame:
    return


# 2. EJERCICIO 2: API DEEZER
# 2.a
def lookup_artist() -> int:
    SCHEME = "https"
    BASE = "api.deezer.com"
    PATH = "/search/artist"
    QUERY = {"q": "Bad Bunny"}

    query_encoded = urlencode(QUERY)
    url = urlunsplit((SCHEME, BASE, PATH, query_encoded, ""))
    response = requests.get(url)
    data = response.json()
    artist_id = data["data"][0]["id"]

    return artist_id

# 2.b

def obtain_top_tracks(artist_id: str) -> dict:
    artist_id = f"{artist_id}"
    SCHEME = "https"
    BASE = "api.deezer.com"
    PATH = "/artist/" + artist_id + "/top"
    QUERY = {"limit": 20}

    query_encoded = urlencode(QUERY)
    url = urlunsplit((SCHEME, BASE, PATH, query_encoded, ""))
    response = requests.get(url)
    data = response.json()

    return data

# 2.c
def transform_to_df(tracks: dict) -> pd.DataFrame:
    filas = []

    for track in tracks["data"]:
        id_deezer = track.get("id", np.nan)
        title = track.get("title", np.nan)
        rank = track.get("rank", 0)
        explicit_lyrics = track.get("explicit_lyrics", np.nan)

        filas.append({
            "id_deezer": id_deezer,
            "title": title,
            "rank": rank,
            "explicit_lyrics": explicit_lyrics
        })

    df = pd.DataFrame(filas)
    df = df.sort_values(by="rank", ascending=False)
    df = df.head(20)

    return df
# 2.d
def group_tracks_by_album(df_tracks: pd.DataFrame) -> pd.DataFrame:
    df_limpio = df_tracks.copy()
    df_limpio = df_limpio.groupby("album").size().reset_index(name="canciones")
    return df_limpio


# 3. EJERCICIO 3: DETECCIÓN DE OUTLIERS

# 3.a
# Use Anderson-Darling test to check if the data follows a normal distribution
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html
# 
# Example usage of stats.anderson:
# {statistic, critical_values, significance_level} = stats.anderson(x)
# Choose the critical value for 5% significance level
def test_anderson_darling(singers: pd.DataFrame) -> bool:
    return

# 3.b
def detect_outliers(singers: pd.DataFrame) -> list:
    media = singers["streams"].mean()
    desviacion = singers["streams"].std()

    z_score = (singers["streams"] - media) / desviacion

    outliers = singers.loc[abs(z_score) > 3, "streams"]

    return outliers