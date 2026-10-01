import pandas as pd
import re


def airbnb_read(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def airbnb_size(df: pd.DataFrame) -> tuple:
    return df.shape


def airbnb_columns(df: pd.DataFrame) -> pd.Index:
    return df.columns


def airbnb_countries(df: pd.DataFrame) -> pd.Series:
    return df["country"].value_counts()


def airbnb_boroughs(df: pd.DataFrame) -> pd.Series:
    df = df.copy()
    df["neighbourhood group"] = df["neighbourhood group"].replace(
        {"brookln": "Brooklyn", "manhatan": "Manhattan"}
    )
    df = df.drop_duplicates(subset=["id"])
    return df["neighbourhood group"].value_counts()


def airbnb_price(df: pd.DataFrame) -> pd.DataFrame:
    prices = df.dropna(subset=["price"])

    if prices["price"].dtype != "float64":
        price_pattern = re.compile("\$((\d+,?)+(\.\d+)?(\s)?)")

        # It is also possible to extract everything with regex, but we have accepted this too.
        convert_price_to_float = lambda x: float(
            price_pattern.match(str(x)).group(1).replace(",", "")
        )
        prices = prices[["price", "neighbourhood group"]]
        prices["price"] = prices["price"].apply(convert_price_to_float)
    return prices


def airbnb_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    df["neighbourhood group"] = df["neighbourhood group"].replace(
        {"brookln": "Brooklyn", "manhatan": "Manhattan"}
    )
    price = airbnb_price(df)[["price", "neighbourhood group"]]
    
    # A lot of you have done this splitting into many functions. 
    # This is valid, but aggregate makes it more simple.
    return price.groupby("neighbourhood group").aggregate(
        ["mean", "median", "std", "min", "max"]
    )


def airbnb_totals(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(airbnb_boroughs(df))


def population_totals(df: pd.DataFrame) -> pd.DataFrame:
    # There is actually data for 2 years in the csv (2000 and 2010)
    population_df = (
        df[df["Year"] == 2010].groupby("Borough")["Population"].sum().reset_index()
    )
    return population_df


def airbnb_population(
    df_airbnb: pd.DataFrame, df_population: pd.DataFrame
) -> pd.DataFrame:
    airbnb_per_borough = df_airbnb.merge(
        df_population, left_on="neighbourhood group", right_on="Borough"
    )
    airbnb_per_borough["Airbnbs per 1000 inhabitants"] = (
        1000 * airbnb_per_borough["count"] / airbnb_per_borough["Population"]
    )
    return airbnb_per_borough
