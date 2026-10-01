import soluciones.crear_fichero_5letras as c
import soluciones.funciones as f

if __name__=="__main__":

    matriz_palabras=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    intentos = 0
    c.limpiar_fichero()
    existe_fichero = f.existencia_fichero()
    palabra_a_adivinar = f.crear_palabra_aleatoria(existe_fichero)
    lista_palabra_objetivo, palabra_objetivo=f.convertir_palabra_objetivo_a_lista(palabra_a_adivinar)
    victoria=False

    while intentos < 5 and not victoria:
        f.solicitar_palabra(intentos,matriz_palabras)
        victoria, intentos=f.comprobar_palabra(lista_palabra_objetivo,intentos,matriz_palabras,victoria)

    f.correcion_de_palabra(palabra_objetivo)
     


            


