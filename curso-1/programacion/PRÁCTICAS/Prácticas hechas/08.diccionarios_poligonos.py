#!/usr/bin/env python
# coding: utf-8

# # Práctica 8. Diccionarios. Figuras.
# 
# ## Enunciado

# ### Objetivos
# - Dominar el concepto de diccionarios.
# - Saber utilizar tuplas.
# - Dominar el flujo de un programa trabajando con menús.
# 
# ## Enunciado de la práctica
# 
# Desarrollar un programa que permita al usuario pintar polígonos a partir de una sucesión de puntos representados en un eje cartesiano.
# 
# Las figuras/polígonos a representar se almacenarán en un diccionario, cuya clave será su nombre (triangulo, cuadrado, pentagono, etc.) y su valor será una lista de tuplas que almacenen sus puntos (x, y).
# 
# Las acciones a realizar vendrán dadas por el siguiente menú. Cada acción realizará únicamente la funcionalidad que se indica y son complementarias entre sí, por lo que pueden seguir el orden que desee el usuario. Por ejemplo, la opción 1 solo caragará los polígonos (no pintará) y la opción 4 dibujará todos los polígonos del diccionario. sea ninguna, porque no se ha pasado antes por la opción 1 o 2, los de por defecto proque se ha pasado por la 1, o todos porque se ha pasado por ambas.
# 
# ### Menu principal
# 
# ```
#          MENU    
#       ==========
#       1. Cargar figuras por defecto
#       2. Crear una nueva figura desde cero
#       3. Dibujar un polígono 
#       4. Dibujar todos los polígonos 
#       
#       9. Salir
# ```
# 
# La **opción 1** creará por defectos dos figuras con los siguiente puntos:
# ```
# Pentágono (x, y)    Triángulo (x, y)    
#     1, 1                2, 2
#     3, 1                2, 4
#     4, 2                5, 5
#     2, 3                2, 2 (se repite el 1º)
#     0, 2
#     1, 1 (se repite el 1º)
# ```
# La **opción 2** pedirá los puntos al usuario para crear una figura/polígono desde cero. El último punto, no será necesario introducirlo, ya que coincide con el primero.
# ```
# Introduzca un nombre de figura: cuadrado
# Introduzca el primer punto x,y (Z para terminar): 1,1
# Siguiente punto x, y (Z para terminar): 1,2
# Siguiente punto x, y (Z para terminar): 2,2
# Siguiente punto x, y (Z para terminar): 2,1
# Siguiente punto x, y (Z para terminar): Z
# ```
# 
# La **opcion 3** dibujará, gracias a la librería matplotlib, solo una figura, la que introduzca el usuario como clave del diccionario.
# ```
# Figura a pintar: cuadrado
# ```
# 
# La **opción 4** pintará todas las figuras que contenga el diccionario.
# 

# ![poligonos.jpg](attachment:poligonos.jpg)

# In[ ]:  


# Importar la biblioteca matplotlib para graficar
import matplotlib.pyplot as plt

# Mostrar el menú
print("   MENU \n =========")
print("1. Cargar figuras por defecto\n2. Crear una nueva figura desde cero\n3. Dibujar un polígono\n4. Dibujar todos los polígonos\n\n9.Salir")

# Inicializar la variable de opción en 0 y el diccionario de figuras vacío
opcion = 0
dict_figuras = {}
finalizado=False

# Bucle principal del programa: se ejecuta mientras la opción no sea 9
while opcion < 10 and not finalizado:
    # Obtener la opción del usuario
    opcion = int(input("Qué opción quieres realizar?: "))
    
    # Opción 1: Cargar figuras por defecto
    if opcion == 1:
        print("Cargamos un pentagono y un triangulo\n==================================", end="\n")
        dict_figuras = {"pentagono": [(1, 1), (3, 1), (4, 2), (2, 3), (0, 2), (1, 1)],
                        "triangulo": [(2, 2), (2, 4), (5, 5), (2, 2)]}

    # Opción 2: Crear una nueva figura desde cero
    elif opcion == 2:
        puntos = []
        nombre = input("¿Cómo se llama la figura quieres representar?: ")
        acabado = False
        while not acabado:
            punto = input("Siguiente punto x,y :")
            print(">>>>>>>>>>>>>>>>>>>>>")
            punto_final = punto.split(",")
            if len(punto_final) == 2:
                x = punto_final[0]
                y = punto_final[1]
                puntos.append((x, y))
            else:
                acabado = True
                print("Tu figura ha sido añadida")
        puntos.append((puntos[0][0], puntos[0][1]))
        dict_figuras[nombre] = puntos 

    # Opción 3: Dibujar un polígono específico
    elif opcion == 3:
        eje_x = []
        eje_y = []
        figura_a_representar = input("Qué figura de las cargadas quieres representar?: ")
        j = 0
        while j < len(dict_figuras[figura_a_representar]):
            eje_x.append(dict_figuras[figura_a_representar][j][0])
            eje_y.append(dict_figuras[figura_a_representar][j][1])
            j += 1
        plt.plot(eje_x, eje_y, color="g")
        plt.show()

    # Opción 4: Dibujar todos los polígonos
    elif opcion == 4:
        for clave, valor in dict_figuras.items():
            x = []
            y = []
            for elem in valor:
                x.append(elem[0])
                y.append(elem[1])
            plt.plot(x, y, color="g")
        plt.show()
        
    # Opción 9: Salir del programa
    elif opcion ==9:
        print("saliendo")
        finalizado=True


