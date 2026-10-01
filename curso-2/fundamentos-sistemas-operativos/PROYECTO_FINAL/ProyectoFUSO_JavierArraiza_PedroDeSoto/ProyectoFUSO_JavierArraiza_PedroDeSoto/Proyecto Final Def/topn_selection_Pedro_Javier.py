import sys

def main():
    if len(sys.argv) != 4:
        print("python3 topn_selection_Pedro_Javier.py <input_file> <top> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    top = int(sys.argv[2])
    output_file = sys.argv[3]

    dicc_usuarios = {}

    with open(input_file, "r", encoding="utf-8") as fichero_entrada:
        for linea in fichero_entrada:
            columnas = linea.strip().split()   # separa por espacio / tabulación

            if not columnas:
                continue

            usuario = columnas[0]

            if usuario in dicc_usuarios:
                dicc_usuarios[usuario] += 1
            else:
                dicc_usuarios[usuario] = 1

    dicc_ordenado = sorted(dicc_usuarios.items(), key=lambda x: x[1], reverse=True)
    top_users = dicc_ordenado[:top]

    with open(output_file, "w", encoding="utf-8") as fichero_salida:
        for user_id, _count in top_users:
            fichero_salida.write(f"{user_id}\n")


if __name__ == "__main__":
    main()
