import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import io
from urllib.parse import urlencode, urlunsplit

url = "https://www.nexford.edu/insights/highest-paying-jobs-in-the-world"


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup



def generate_database(soup: BeautifulSoup) -> pd.DataFrame:
    trabajos = soup.find_all("h3")
    salarios = soup.find_all("a")
    filas = []
    salario = []
    trabajo = []
    for c1 in salarios:
        c1.get_text(strip=True)
        salario.append(c1)
    for c2 in trabajos:
        c2.get_text(strip=True)
        trabajo.append(c2)

    filas.append({
        "Trabajo" : trabajo,
        "salario": salario
    })
    df = pd.DataFrame(filas)
    df["Trabajo"] = df["Trabajo"].str.extract(r"\.\s(.+)")
    

    





def obtain_numeric_salary(best_jobs_1c: pd.DataFrame) -> pd.DataFrame:
    pass

#ejercicio 2
def get_data_scientist_jobs() -> pd.DataFrame:
    pass


#ejercicio 3
def impute_outliers(all_jobs_3a: pd.DataFrame) -> pd.DataFrame:
    pass

def impute_missing(all_jobs_3b: pd.DataFrame) -> pd.DataFrame:
    pass

#ejercicio 4

def compare_sources(best_jobs_4: pd.DataFrame, 
                    all_jobs_4: pd.DataFrame) -> pd.DataFrame:
    pass


    

