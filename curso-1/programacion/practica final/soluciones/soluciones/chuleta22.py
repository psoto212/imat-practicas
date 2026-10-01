import random
import sys

def load_data(fichero = 'configuracion.txt'):
    with open(fichero, 'r') as file:
        # dim_tablero = int(file.readline())

        # mines = int(file.readline())
        dim_tablero, mines = file.readlines()
        dim_tablero = int(dim_tablero)
        mines = int(mines)
    return dim_tablero, mines

def create_mines(dim_tablero, mines):
    tablero_minas = [[0 for col in range(dim_tablero)] for row in range(dim_tablero)]
    minas_colocadas = 0
    if mines > dim_tablero ** 2:
        raise Exception('Hay demasiadas minas')
    while mines != minas_colocadas:
        i = random.randint(0, dim_tablero - 1)
        j = random.randint(0, dim_tablero - 1)

        # Solo asignamos la mina si la posición estaba vacía
        if tablero_minas[i][j] == 0:
            minas_colocadas += 1
            tablero_minas[i][j] = 1
    return tablero_minas


def create_prox(dim_tablero, tablero_minas):
    '''
        Función para asignar a las casillas el número 
        de minas que tienen a su alrededor
    '''

    # Inicializamos el tablero de proximidades
    tablero_proximidades = [[0 for col in range(dim_tablero)] for row in range(dim_tablero)]
    
    # Iteramos por el tablero en busca de minas
    for row in range(dim_tablero):
        for col in range(dim_tablero):
            if tablero_minas[row][col] == 1:
                
                # Si encontramos una mina:
                # Miramos alrederor de la casilla mina y sumamos 1 a cada una
                for i in range(-1, 2):
                    new_x = row + i
                    for j in range(-1, 2):
                        new_y = col + j

                        # Comprobar si la posición nueva está dentro del tablero
                        if new_x >= 0 and new_x < dim_tablero and new_y >= 0 and new_y < dim_tablero:
                            tablero_proximidades[row+i][col+j] += 1
    return tablero_proximidades


def create_board(dim_tablero, mines):
    tablero = [['##' for col in range(dim_tablero)] for row in range(dim_tablero)]
    tablero_minas = create_mines(dim_tablero, mines)
    tablero_proximidades = create_prox(dim_tablero, tablero_minas)
    return tablero, tablero_minas, tablero_proximidades

def pintar(tablero):
    for fila in tablero:
        print(fila)


def victoria(tablero, mines):
    '''

        Recorrer el tablero en busca de ##, 
        si hay el mismo numero que mines, return True

    '''
    hastag_count = 0
    for row in tablero:
        for element in row:
            if element == '##':
                hastag_count += 1

    if hastag_count == mines:
        return True

    return False

class ConfigurationError(Exception):
    pass

if __name__ == '__main__':

    ficheros = {'grande': 'grande.txt', 'pequeño': 'pequeño.txt'}
    

    try:
        nombre_fichero = ficheros[sys.argv[1]]
    except KeyError:
        raise ConfigurationError('Configuración no existe')

    dim_tablero, mines = load_data(nombre_fichero)

    tablero, tablero_minas, tablero_proximidades = create_board(dim_tablero, mines)
    
    salir = False
    posiciones = [-1, 0, 1]

    while not salir:
        coords = input('Introduzca las coordenadas i,j : ')
        if coords == 'salir':
            salir = True
            continue
        row, col = coords.split(',')
        row = int(row)
        col = int(col)
        if tablero_minas[row][col] == 1:
            print('HAS PERDIDO')
            salir = True
            continue
        else:
            for i in posiciones:
                new_x = row + i
                for j in posiciones:
                    new_y = col + j

                    if new_x >= 0 and new_x < dim_tablero and new_y >= 0 and new_y < dim_tablero:
                        if tablero_minas[new_x][new_y] == 0:
                            tablero[new_x][new_y] = ' ' + str(tablero_proximidades[new_x][new_y])

            pintar(tablero)
            if victoria(tablero, mines):
                print('HAS GANADO')
                salir = True



