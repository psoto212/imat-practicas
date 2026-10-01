#!/bin/bash

n1=10
n2=5

for funcion in "suma" "resta" "multiplicacion" "division"
do
		python3 ejemplo_python_bash.py -funcion $funcion -primer_numero $n1 -segundo_numero $n2
done
