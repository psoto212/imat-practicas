from jugador import Jugador
from registro import Registro

class Partida:
    def __init__(self, jugador1, jugador2, n_barcos):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.n_barcos = n_barcos
        self.turno = 1
        self.registro = Registro()

    def iniciar_partida(self):
        print(f"{self.jugador1.nombre}, coloca tus barcos")
        self.jugador1.colocar_barcos(self.n_barcos)

        print(f"{self.jugador2.nombre}, coloca tus barcos")
        self.jugador2.colocar_barcos(self.n_barcos)

        terminado = False
        while not terminado:
            if self.turno % 2 != 0:
                print(f"Turno de {self.jugador1.nombre}")
                estado = self.jugador1.atacar(self.jugador2)
            else:
                print(f"Turno de {self.jugador2.nombre}")
                estado = self.jugador2.atacar(self.jugador1)

            self.jugador1.tablero.dibujar(self.jugador2.tablero)
            self.jugador2.tablero.dibujar(self.jugador1.tablero)

            if self.jugador1.tablero.matriz.count("X") == self.n_barcos:
                print(f"{self.jugador1.nombre} ha ganado la partida!")
                self.registro.guardar_registro(self.jugador1, self.jugador2, self.jugador1.nombre)
                terminado = True
            elif self.jugador2.tablero.matriz.count("X") == self.n_barcos:
                print(f"{self.jugador2.nombre} ha ganado la partida!")
                self.registro.guardar_registro(self.jugador1, self.jugador2, self.jugador2.nombre)
                terminado = True

            self.turno += 1
