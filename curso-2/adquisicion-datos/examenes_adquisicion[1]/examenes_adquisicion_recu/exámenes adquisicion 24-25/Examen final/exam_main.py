import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import io
from urllib.parse import urlencode, urlunsplit

REGEX_SALARY = re.compile(r"\$(\d+),(\d+)")
REGEX_JOBS = re.compile(r"\d{1,2}. ([A-Za-z ]*)(\\xa0)?")

# 1
# 1.a
def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    return soup

# 1.b
def generate_database(soup: BeautifulSoup) -> pd.DataFrame:
    trabajos_busqueda = soup.findAll(name="h3")
    salarios_busqueda = soup.findAll(name="a")

    salarios = []
    for salario in salarios_busqueda:
        if re.search(REGEX_SALARY, salario.text):
            salarios.append(salario)
    salarios = salarios[:15]

    trabajos=[]
    for trabajo in trabajos_busqueda:
        if re.search(REGEX_JOBS, trabajo.text):
            trabajo_regex = re.search(REGEX_JOBS, trabajo.text).group(1)
            trabajos.append(trabajo_regex)
    trabajos = trabajos[:15]

    df = pd.DataFrame(salarios, index=trabajos, columns=["salario"])
    return df

# 1.c
def obtain_numeric_salary(best_jobs_1c: pd.DataFrame) -> pd.DataFrame:
    best_jobs_1c["salario"] = best_jobs_1c["salario"].apply(lambda x: int(re.search(REGEX_SALARY, x).group(1)+re.search(REGEX_SALARY, x).group(2)))
    return best_jobs_1c


# 2
def get_data_scientist_jobs() -> pd.DataFrame:
    SCHEME = "https"
    BASE = "jobicy.com/api/v2"
    PATH = "/remote-jobs"
    QUERY = {"tag":"data scientist"}

    query_encoded =  urlencode(QUERY)

    url=urlunsplit((SCHEME, BASE, PATH, query_encoded, ""))
    response=requests.get(url)

    df = pd.DataFrame.from_dict(response.json())

    data = []
    for _, rows in df.iterrows():
        industry = rows["jobs"]["jobIndustry"][0]
        if "annualSalaryMin" in rows["jobs"]:
            salary = rows["jobs"]["annualSalaryMin"]
        else:
            salary = np.nan
        
        data.append(("data scientist", industry, salary))
        
    df_final = pd.DataFrame(data)
    return df_final


# 3
# 3.a
def impute_outliers(all_jobs_3a: pd.DataFrame) -> pd.DataFrame:
    # Calculo de z_score
    all_jobs_3a["z_score_salary"] = (all_jobs_3a.salary - all_jobs_3a.salary.mean())/all_jobs_3a.salary.std()
    
    median = all_jobs_3a["salary"].median()
    all_jobs_3a["salary"].loc[all_jobs_3a["z_score_salary"].abs() > 3] = median

    return all_jobs_3a[["job", "industry", "salary"]]

# 3.b
def impute_missing(all_jobs_3b: pd.DataFrame) -> pd.DataFrame:
    all_jobs_3b["salary"] = all_jobs_3b.groupby("industry")["salary"].apply(lambda x: x.fillna(x.median())).reset_index(level=0, drop=True)

    return all_jobs_3b


# 4
def compare_sources(best_jobs_4: pd.DataFrame, 
                    all_jobs_4: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.merge(best_jobs_4, all_jobs_4)
    df_merged["variation"] = (df_merged["salary"]-df_merged["salary_average"])/df_merged["salary"]
    df_merged = df_merged[["job", "variation"]]
    df_merged = df_merged.groupby("job").mean().variation.sort_values(ascending=False).reset_index()
    return df_merged

if __name__ == "__main__":
    #print(get_soup("https://www.nexford.edu/insights/highest-paying-jobs-in-the-world").prettify())
    #soup = get_soup("https://www.nexford.edu/insights/highest-paying-jobs-in-the-world")
    #df = generate_database(soup)
    #print(df)
    #df_numeric = obtain_numeric_salary(df)
    #print(df)

    #df_ouliers = pd.read_csv("all_jobs_3a.csv", sep=";")
    #df_ouliers = impute_outliers(df_ouliers)
    #print(df_ouliers)
    #print("__________________")
    #df_ouliers = impute_missing(df_ouliers)
    #print(df_ouliers)

    #df_best = pd.read_csv("best_jobs_4.csv", sep=";")
    #df_all = pd.read_csv("all_jobs_4.csv", sep=";")
    #df_compare = compare_sources(df_best, df_all)
    #print(df_compare)

    #df = get_data_scientist_jobs()
    #print(df)

    pass