import pandas as pd
import os

path = "cities.csv"
size = os.stat(path).st_size
print("Tamaño en disco:", size, "bytes")

df = pd.read_csv(path)
print("\n== Tamaño en memoria inicial ==")
print(df.info(memory_usage='deep'))

print("\nUso por columna:")
print(df.memory_usage(deep=True))

df_opt = df.copy()

for col in df_opt.columns:
    if pd.api.types.is_numeric_dtype(df_opt[col]):
        df_opt[col] = pd.to_numeric(df_opt[col], downcast='integer')
        df_opt[col] = pd.to_numeric(df_opt[col], downcast='float')

print("\n== Tamaño en memoria tras optimización ==")
print(df_opt.info(memory_usage='deep'))

print("\nUso por columna optimizada:")
print(df_opt.memory_usage(deep=True))

print("\nComentario:")
print("Usar dtype= en read_csv es mejor porque reduce memoria desde el principio.")
