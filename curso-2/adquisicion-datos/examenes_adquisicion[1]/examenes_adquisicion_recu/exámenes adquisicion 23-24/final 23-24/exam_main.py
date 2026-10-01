import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlunsplit, urlencode


#### Part 1 ####


def fetch_holidays(year: int, country_iso: str) -> list[dict]:
    SCHEME = 'https'
    BASE= 'date.nager.at/api'
    PATH = f'/v3/PublicHolidays/{year}/{country_iso}'
    def get_url(path,query_dict=None):
        if query_dict is None:
            query_dict = {}
        query = urlencode(query_dict)
        return urlunsplit((SCHEME,BASE,PATH,query,''))
    response = requests.get(get_url(PATH))
    return response.json()

def transform_holidays(response_json: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(response_json)
    return None


def scrape_communities() -> pd.DataFrame:
    
    return 


def combine_data(api_df: pd.DataFrame, wikipedia_df: pd.DataFrame) -> pd.DataFrame:    
    
    return


def max_holidays_community(df: pd.DataFrame) -> str:
    
    comunity = "# TODO"
    festivities = "# TODO"
    return f"La comunidad autónoma con más festivos es {comunity} con {festivities} festivos."


def min_holidays(df: pd.DataFrame) -> int:
    
    comunity = "# TODO"
    festivities = "# TODO"
    return f"La comunidad autónoma con más festivos es {comunity} con {festivities} festivos."


#### Part 2 ####


def income_imputation(df: pd.DataFrame) -> pd.DataFrame: 
       
    return 


def outlier_detection(df: pd.DataFrame) -> pd.DataFrame:
    
    return


def phone_number(df: pd.DataFrame) -> pd.DataFrame:
    
    return

if __name__ == "__main__":
    fiestas_dict = fetch_holidays(2024, "ES")
    print(fiestas_dict)
