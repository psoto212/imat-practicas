class Tablero:
    def __init__(self):
        self.matriz = ["0"] * 100

    def dibujar(self, tablero_oponente):
        print("\t     Tablero jugador 1\t\t\t\t\t\t\t     Tablero jugador 2")
        print("  "+"   ".join([str(x) for x in range(1, 11)]), end="")
        print("\t\t\t\t  "+"   ".join([str(x) for x in range(1, 11)]), end="")
        for idx, let in enumerate("ABCDEFGHIJ"):
            print("\n" + let, end=" ")
            print(" | ".join(self.matriz[10*idx:10*(idx+1)]), end=" |")
            print("\t\t\t\t" + let, end=" ")
            print(" | ".join(tablero_oponente.matriz[10*idx:10*(idx+1)]), end=" |")
            print("\n  --------------------------------------", end="")
            print("\t\t\t\t  --------------------------------------", end="")

    def comprobar_colocar_barco(self, fila, columna, direccion, longitud):
        dic = {"a": 0, "b": 10, "c": 20, "d": 30, "e": 40, "f": 50, "g": 60, "h": 70, "i": 80, "j": 90}
        if direccion == "h":
            if 0 < (dic[fila] + columna + longitud) % 10 < longitud:
                return False
            return all(self.matriz[dic[fila] + columna + i] == "0" for i in range(longitud))
        else:
            if (dic[fila] + columna) // 10 + longitud > 10:
                return False
            return all(self.matriz[dic[fila] + columna + 10 * i] == "0" for i in range(longitud))

    def colocar_barco(self, fila, columna, direccion, longitud):
        dic = {"a": 0, "b": 10, "c": 20, "d": 30, "e": 40, "f": 50, "g": 60, "h": 70, "i": 80, "j": 90}
        if direccion == "h":
            for i in range(longitud):
                self.matriz[dic[fila] + columna + i] = "1"
        else:
            for i in range(longitud):
                self.matriz[dic[fila] + columna + 10 * i] = "1"

    def atacar(self, fila, columna):
        dic = {"a": 0, "b": 10, "c": 20, "d": 30, "e": 40, "f": 50, "g": 60, "h": 70, "i": 80, "j": 90}
        indice = dic[fila] + columna
        if self.matriz[indice] == "0":
            self.matriz[indice] = "A"
            return "A"
        else:
            self.matriz[indice] = "X"
            return "X"
