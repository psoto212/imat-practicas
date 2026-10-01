"""
imatlab.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GP18A
Integrantes:
    - JORGE FERNÁNDEZ PUIG
    - LUIS CASTILLO SÁNCHEZ

Descripción:
Sistema interactivo IMAT-LAB de resolución de ecuaciones en aritmética modular.

Interfaz de acceso interactivo o por lotes a la librería modular.py. Si este script se ejecuta sin par´ametros,
lanzar´a la interfaz de usuario para el modo interactivo.
"""

from typing import TextIO
from modular import*
import sys



""" Recibe un manejador fin de un fichero de texto ya abierto para lectura y otro de un fichero de salida
ya abierto para escritura y ejecuta línea por línea los comandos proporcionados por fin, escribiendo los resultados en fout. Si
fin y fout no corresponden con la entrada y salida esáandar, esta función ejecuta el modo de procesamiento
por lotes de IMAT-LAB para la entrada fin, guardando el resultado en el fichero fout.

    Args:
        fin (TextIO): Fichero de entrada. Manejador de un fichero de texto ya abierto para lectura.
        fout (TextIO): Fichero de salida. Manejador de un fichero de texto ya abierto para escritura.
    
    Returns: None
    
    Raises: None
    
    Examples:
        run_commands(sys.stdin,sys.stdout) lanza el modo interactivo y ejecuta línea por línea los comandos que
            el usuario lanza desde la entrada estándar.
"""
def run_commands(fin:TextIO,fout:TextIO):
    for line in fin:
        command = line.strip()
        
        if not command:
            continue  # Si la línea está vacía, continúa con la siguiente

        try:
            # Ejecutar el comando. Por ejemplo, resolver ecuaciones modulares
            result = eval(command)  # Se puede ajustar para funciones específicas
            fout.write(f"Resultado: {result}\n")
        
        except Exception as e:
            fout.write(f"Error al procesar el comando '{command}': {str(e)}\n")

if __name__ == "__main__":
    """
    Función principal que gestiona los modos interactivo y por lotes.
    """

    if len(sys.argv) == 1:
        # Modo interactivo
        print("Entrando en modo interactivo. Escriba 'exit' para salir.")
        while True:
            command = input(">> ")
            if command.lower() == 'exit':
                break
            try:
                result = eval(command)
                print(f"Resultado: {result}")
            except Exception as e:
                print(f"Error: {str(e)}")

    elif len(sys.argv) == 3:
        # Modo batch (por lotes)
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        try:
            with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
                run_commands(fin, fout)
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")
    else:
        print("Uso: python imatlab.py [input_file output_file]")
