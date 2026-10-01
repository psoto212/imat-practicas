import pandas as pd


def unique_radars(archivo):
    df = pd.read_csv(archivo)
    radares_unicos = df.unique()
    df = radares_unicos
    return df











if __name__ == "__main__":
    archivo = "radars.csv"
    print(unique_radars(archivo))