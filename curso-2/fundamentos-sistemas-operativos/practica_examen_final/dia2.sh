#!/bin/bash

mkdir -p experimentos
mkdir -p filtrados
mkdir -p copias

global="global.csv"
resumen="resumen.txt"
fallos="fallos.csv"
numeros="numeros.txt"

if [ -f "$global" ]; then
    rm "$global"
fi
if [ -f "$resumen" ]; then
    rm "$resumen"

fi

primero=1
for algoritmo in FCFS SJF RR HRRN
do
    for quantums in 2 4 6 8
    do
        if [[ algoritmo=="FCFS" && quantums -eq 8 ]]; then
            echo "saltando fcfs quantum 8"
        else
            fichero="experimentos/${algoritmo}_${quantums}.csv"
            echo "algoritmo;quantum;estado;tiempo" > "$fichero"
            echo "$algoritmo;$quantums;OK;${quantum}00" >> "$fichero$"
            echo "$algoritmo;$quantums;FALLO;${quantum}99" >> "$fichero$"

            if [[ primero -eq 1 ]]; then
                cat "$fichero" > "$global"
                primero=0
            else
                tail -n +2 "$fichero" >> "$global"

            
            fi
        fi
    done
done

grep "FALLO" "$global" > "$fallos"

contador=$(grep "ERROR" "$fallos"|wc -l)












   