from tablero import Tablero

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.barcos_colocados = 0

    def colocar_barcos(self, n_barcos, max_longitud=5):
        for i in range(n_barcos):
            valido = False
            while not valido:
                try:
                    fila = input(f"{self.nombre}, introduce la fila del barco {i + 1} (A-J): ").lower()
                    columna = int(input(f"Introduce la columna del barco {i + 1} (1-10): ")) - 1
                    direccion = input(f"Introduce la direccion del barco {i + 1} (v/h): ").lower()

                    if fila not in "abcdefghij" or direccion not in "vh" or not (0 <= columna < 10):
                        print("Entrada no valida. Intente de nuevo.")
                        continue

                    longitud = int(input(f"Introduce la longitud del barco {i + 1} (1-{max_longitud}): "))
                    if longitud < 1 or longitud > max_longitud:
                        print(f"Longitud no válida. Debe ser entre 1 y {max_longitud}.")
                        continue

                    # Comprobar si se puede colocar el barco
                    if self.tablero.comprobar_colocar_barco(fila, columna, direccion, longitud):
                        self.tablero.colocar_barco(fila, columna, direccion, longitud)
                        self.barcos_colocados += 1
                        valido = True
                        print(f"Barco {i + 1} colocado en {fila.upper()} {columna + 1} hacia {direccion} con longitud {longitud}.")
                    else:
                        print(f"No se puede colocar el barco {i + 1} en esa posición. Intente nuevamente.")
                except ValueError:
                    print("Entrada no válida. Intente de nuevo.")

    def atacar(self, oponente):
        fila = input(f"{self.nombre}, introduce la fila del ataque (A-J): ").lower()
        columna = int(input(f"Introduce la columna del ataque (1-10): ")) - 1

        if fila not in "abcdefghij" or not (0 <= columna < 10):
            print("Entrada no válida. Intente de nuevo.")
            return None

        resultado = oponente.tablero.atacar(fila, columna)
        if resultado == "A":
            print(f"{self.nombre} ha fallado el ataque.")
        else:
            print(f"{self.nombre} ha acertado el ataque.")
        return resultado
