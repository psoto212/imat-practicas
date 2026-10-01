#!/bin/bash

n1="10 20"
n2=5

for n in $n1
do
	for funcion in "suma" "resta" "multiplicacion" "division"
	do
			python3 ejemplo_python_bash.py -funcion $funcion -primer_numero $n -segundo_numero $n2
	done
done
