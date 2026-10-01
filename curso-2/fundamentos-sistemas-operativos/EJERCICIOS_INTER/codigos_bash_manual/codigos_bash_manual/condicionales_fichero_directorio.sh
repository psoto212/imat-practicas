#!/bin/bash
fichero=salida.txt
if [ -f "$fichero" ]; then
    echo "El fichero $fichero existe."
else
    echo "El fichero $fichero NO existe."
fi

dir=directorio
if [ -d "$dir" ]; then
    echo "El directorio $dir existe."
fi

STR="El modelo de vecinos proximos es un modelo de IA"
SUB="IA"
if [[ "$STR" == *"$SUB"* ]]; then
  echo "Esta contenido"
fi

STR="El modelo de vecinos proximos es un modelo de IA"
SUB="EL"
if [[ "$STR" == "$SUB"* ]]; then
  echo "$STR comienza por $SUB"
fi
