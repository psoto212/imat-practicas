import pandas as pd
import re

DATE_CONVERSION = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}


# Q1
def read_dataset(path: str) -> tuple[pd.DataFrame, tuple[int, int]]:
    return


def ensure_all_registers_unique(df_sp: pd.DataFrame) -> bool:
    return


def fix_data_providers(df_sp: pd.DataFrame) -> pd.DataFrame:
    return


# Q2


def correct_dates(df_sp_2: pd.DataFrame) -> pd.DataFrame:
    return


# Q3


def plot_boxplot(df_inflation: pd.DataFrame) -> None:
    return


def find_anomalous_days(df_inflation: pd.DataFrame) -> list[str]:
    return


# Q4


def correct_inflation(
    df_inflation: pd.DataFrame, df_sp_4: pd.DataFrame
) -> pd.DataFrame:
    return
