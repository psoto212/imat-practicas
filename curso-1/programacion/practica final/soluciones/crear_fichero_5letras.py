
def limpiar_fichero():
    """
    realizamos un data_cleaning al pasar las palabras de 5 letras del fichero palabras.txt, y 
    cambiar los caracteres de aquellas palabras que contienen tildes por su correspondiente caracter sin tilde de dicho fichero,
    al fichero palabras_worldlet.txt
    """
    fichero_palabras=open("palabras.txt", "r", encoding="utf-8")
    fichero_final=open("palabras_worldlet.txt", "w", encoding="utf-8")
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 
              'ü': 'u', 'ñ': 'n', 'Á': 'A', 'É': 'E', 'Í': 'I', 
              'Ó': 'O', 'Ú': 'U', 'Ü': 'U', 'Ñ': 'N'}
    for palabra in fichero_palabras:
         palabra_acotada=palabra.strip("\n")
         if len(palabra_acotada)==5:
             palabra_sin_tilde=""
             for caracter in palabra_acotada:
                  if caracter in tildes:
                       palabra_sin_tilde += tildes[caracter]
                  else:
                       palabra_sin_tilde += caracter
             fichero_final.write(palabra_sin_tilde)
             fichero_final.write("\n")
