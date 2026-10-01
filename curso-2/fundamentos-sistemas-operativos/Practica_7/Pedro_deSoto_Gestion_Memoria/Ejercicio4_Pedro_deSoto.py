import pandas as pd


df = pd.read_csv("custom_1988_2020.csv", nrows=20_000_000)



def create_list(df):

    valores = df["ym"].unique()
    lista = [df[df["ym"] == val].copy() for val in valores]
    return lista


def create_generator(df):
    
    valores = df["ym"].unique()
    for val in valores:
        yield df[df["ym"] == val].copy()



from memory_profiler import profile

@profile
def procesar(df, modo):

    if modo == "lista":
        iterador = create_list(df)
    else:
        iterador = create_generator(df)

    resultados = []
    for elemento in iterador:
        resultados.append(elemento["value"].sum())

    return resultados



if __name__ == "__main__":

    import sys
    if len(sys.argv) > 1:
        modo = sys.argv[1]
        procesar(df, modo)
    else:
        print("Usa: python Ejercicio4_TuNombre.py lista")
        print("   o: python Ejercicio4_TuNombre.py generador")
