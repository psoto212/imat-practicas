# main.py
from partida import Partida
from jugador import Jugador
from registro import Registro

def main():
    nombre_j1 = input("Introduce el nombre del Jugador 1: ")
    nombre_j2 = input("Introduce el nombre del Jugador 2: ")

    jugador1 = Jugador(nombre_j1)
    jugador2 = Jugador(nombre_j2)

    n_barcos = int(input("Introduce el numero de barcos (2-4): "))

    partida = Partida(jugador1, jugador2, n_barcos)
    partida.iniciar_partida()

    # Mostrar registros de partidas
    registro = Registro()
    registro.mostrar_registros()

if __name__ == "__main__":
    main()

