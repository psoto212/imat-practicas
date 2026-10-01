import sys
import argparse


def suma(n1: float, n2: float, debug:bool=False) -> float:
    """
        :param n1: primer numero
        :param n2: segundo numero

        :return la suma entre los numeros
    """
    print("suma")
    print(n1 + n2)


def resta(n1: float, n2: float, debug:bool=False) -> float:
    """
        :param n1: primer numero
        :param n2: segundo numero

        :return la resta entre los numeros
    """
    print("resta")
    print(n1 - n2)

def multiplicacion(n1: float, n2: float, debug:bool=False) -> float:
    """
        :param n1: primer numero
        :param n2: segundo numero

        :return la multiplicacion entre los numeros
    """
    print("multiplicacion")
    print(n1 * n2)


def division(n1: float, n2: float, debug:bool=False) -> float:
    """
        :param n1: primer numero
        :param n2: segundo numero

        :return la division entre los numeros
    """
    print("division")
    print(n1 / n2)


if __name__ == "__main__":
    debug = False
    # Creamos el procesador de argumentos
    parser = argparse.ArgumentParser()

    # Agregamos los argumentos
    parser.add_argument('-funcion', type=str, help='Funcion a ejecutar')
    parser.add_argument('-primer_numero', type=float, help='primer numero')
    parser.add_argument('-segundo_numero', type=float, help='segundo numero')

    parser.add_argument('--debug', type=bool, help='debug')

    # Parsear los argumentos de la linea de comandos
    args = parser.parse_args()

    funcion = args.funcion
    n1 = args.primer_numero
    n2 = args.segundo_numero

    if args.debug:
        debug = args.debug

    if funcion == "suma":
        suma(n1, n2, debug)
    elif funcion == "resta":
        resta(n1, n2, debug)
    elif funcion == "multiplicacion":
        multiplicacion(n1, n2, debug)
    elif funcion == "division":
        division(n1, n2, debug)
    else:
        print("Opcion no reconocida")
