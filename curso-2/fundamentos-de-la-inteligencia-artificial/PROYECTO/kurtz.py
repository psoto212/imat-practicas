# kurtz.py
# Fundamentos de IA - Proyecto (Parte 1)
# Versión clara, funcional y de nivel medio-alto
# Ejecuta: python kurtz.py

import random
from collections import deque

TAMANO = 6  # Mapa 6x6


# ============================
# Funciones básicas
# ============================
def dentro_del_mapa(fila, columna):
    return 0 <= fila < TAMANO and 0 <= columna < TAMANO


def vecinos_en_cruz(fila, columna):
    for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nf, nc = fila + df, columna + dc
        if dentro_del_mapa(nf, nc):
            yield (nf, nc)


def paredes_en_posicion(fila, columna):
    return (
        fila == 0,
        fila == TAMANO - 1,
        columna == 0,
        columna == TAMANO - 1
    )


def bfs_camino(inicio, objetivo, celdas_permitidas):
    if inicio == objetivo:
        return [inicio]

    cola = deque([inicio])
    padre = {inicio: None}

    while cola:
        actual = cola.popleft()
        for vecino in vecinos_en_cruz(*actual):
            if vecino in padre:
                continue
            if vecino not in celdas_permitidas:
                continue
            padre[vecino] = actual
            if vecino == objetivo:
                camino = []
                nodo = vecino
                while nodo is not None:
                    camino.append(nodo)
                    nodo = padre[nodo]
                camino.reverse()
                return camino
            cola.append(vecino)
    return None


# ============================
# Mundo (entorno real)
# ============================
class Mundo:
    def __init__(self):
        self.posicion_inicial = (0, 0)
        self.precipicios = set()
        self.posicion_soldado = None
        self.soldado_vivo = True
        self.posicion_salida = None
        self.posicion_kurtz = None
        self.generar_mapa()

    def celda_aleatoria(self, ocupadas):
        while True:
            f = random.randint(0, TAMANO - 1)
            c = random.randint(0, TAMANO - 1)
            if (f, c) not in ocupadas:
                return (f, c)

    def generar_mapa(self):
        ocupadas = {self.posicion_inicial}

        while len(self.precipicios) < 3:
            self.precipicios.add(self.celda_aleatoria(ocupadas | self.precipicios))
        ocupadas |= self.precipicios

        self.posicion_soldado = self.celda_aleatoria(ocupadas)
        ocupadas.add(self.posicion_soldado)

        self.posicion_salida = self.celda_aleatoria(ocupadas)
        ocupadas.add(self.posicion_salida)

        self.posicion_kurtz = self.celda_aleatoria(ocupadas)

    def muerte_en_celda(self, posicion):
        if posicion in self.precipicios:
            return True, "Has caído en un precipicio"
        if self.soldado_vivo and posicion == self.posicion_soldado:
            return True, "El soldado te ha matado"
        return False, ""

    def obtener_percepto(self, posicion, hubo_grito=False):
        f, c = posicion
        brisa = any(v in self.precipicios for v in vecinos_en_cruz(f, c))
        ronquido = self.soldado_vivo and any(v == self.posicion_soldado for v in vecinos_en_cruz(f, c))
        resplandor = posicion == self.posicion_salida or any(v == self.posicion_salida for v in vecinos_en_cruz(f, c))
        p_arr, p_ab, p_iz, p_der = paredes_en_posicion(f, c)

        percepto_lista = [
            brisa, ronquido, resplandor,
            p_arr, p_ab, p_iz, p_der,
            hubo_grito
        ]

        percepto_diccionario = {
            "brisa": brisa,
            "ronquido": ronquido,
            "resplandor": resplandor,
            "pared_arriba": p_arr,
            "pared_abajo": p_ab,
            "pared_izquierda": p_iz,
            "pared_derecha": p_der,
            "grito": hubo_grito
        }

        return percepto_lista, percepto_diccionario

    def mover(self, posicion, direccion):
        movimientos = {"W": (-1, 0), "S": (1, 0), "A": (0, -1), "D": (0, 1)}
        df, dc = movimientos[direccion]
        nf, nc = posicion[0] + df, posicion[1] + dc
        if not dentro_del_mapa(nf, nc):
            return posicion, True
        return (nf, nc), False

    def lanzar_granada(self, posicion, direccion):
        if not self.soldado_vivo:
            return False
        movimientos = {"W": (-1, 0), "S": (1, 0), "A": (0, -1), "D": (0, 1)}
        df, dc = movimientos[direccion]
        objetivo = (posicion[0] + df, posicion[1] + dc)
        if objetivo == self.posicion_soldado:
            self.soldado_vivo = False
            return True
        return False


# ============================
# Agente
# ============================
class Agente:
    def __init__(self):
        self.posicion = (0, 0)
        self.visitadas = {self.posicion}
        self.sin_precipicio = {self.posicion}
        self.sin_soldado = {self.posicion}
        self.tiene_granada = True
        self.kurtz_encontrado = False

    def es_segura(self, celda):
        return celda in self.sin_precipicio and celda in self.sin_soldado


# ============================
# Modo manual
# ============================
def modo_manual():
    mundo = Mundo()
    agente = Agente()
    hubo_grito = False

    while True:
        muerto, mensaje = mundo.muerte_en_celda(agente.posicion)
        if muerto:
            print("\nGAME OVER:", mensaje)
            return

        if agente.posicion == mundo.posicion_kurtz:
            agente.kurtz_encontrado = True
            print("\nHas encontrado a Kurtz")

        if agente.posicion == mundo.posicion_salida and agente.kurtz_encontrado:
            print("\n¡Has salido con Kurtz! VICTORIA")
            return

        percepto_lista, _ = mundo.obtener_percepto(agente.posicion, hubo_grito)
        hubo_grito = False

        f, c = agente.posicion
        print(f"\nPosición: ({f+1},{c+1})")
        print("Percepto:", percepto_lista)
        print("WASD mover | G+WASD granada | Q salir")

        accion = input("Acción: ").upper()

        if accion == "Q":
            return

        if accion.startswith("G") and agente.tiene_granada:
            direccion = accion[1]
            agente.tiene_granada = False
            if mundo.lanzar_granada(agente.posicion, direccion):
                print("Soldado eliminado")
                hubo_grito = True
            continue

        if accion in "WASD":
            nueva, pared = mundo.mover(agente.posicion, accion)
            if not pared:
                agente.posicion = nueva
                agente.visitadas.add(nueva)
                agente.sin_precipicio.add(nueva)
                agente.sin_soldado.add(nueva)


# ============================
# Programa principal
# ============================
def main():
    print("Proyecto FIA - Kurtz")
    print("Modo manual")
    modo_manual()


if __name__ == "__main__":
    main()
