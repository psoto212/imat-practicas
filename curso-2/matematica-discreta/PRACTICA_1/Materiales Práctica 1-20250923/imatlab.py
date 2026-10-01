"""
imatlab.py
"""

from typing import TextIO
from modular import *
import sys

def run_commands(fin: TextIO, fout: TextIO):
    for line in fin:
        command = line.strip()
        if not command:
            continue
        try:
            result = eval(command)
            if result is True:
                fout.write("Sí\n")
            elif result is False:
                fout.write("No\n")
            elif isinstance(result, dict):
                if result:
                    fout.write(", ".join(f"{p}: {e}" for p, e in sorted(result.items())) + "\n")
                else:
                    fout.write("\n")
            elif isinstance(result, tuple) and len(result) == 2 and isinstance(result[1], int):
                fout.write(f"{result[0]} (mod {result[1]})\n")
            else:
                fout.write(str(result) + "\n")
        except IncompatibleEquationError:
            fout.write("NE\n")
        except Exception:
            fout.write("NOP\n")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Entrando en modo interactivo. Escriba 'exit' para salir.")
        while True:
            command = input(">> ")
            if command.lower() == 'exit':
                break
            try:
                result = eval(command)
                print(result)
            except Exception:
                print("NOP")
    elif len(sys.argv) == 3:
        input_file, output_file = sys.argv[1], sys.argv[2]
        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            run_commands(fin, fout)
    else:
        print("Uso: python imatlab.py [input_file output_file]")
