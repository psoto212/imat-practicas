#!/bin/bash

bienvenida="Estimado usuario"
usuario=$(whoami)
fecha=$(date)

echo "$bienvenida $usuario,"
echo "Hoy es $fecha"
echo "Esperemos que tenga un buen dia"

echo "podemos concatenar cadenas de esta forma $usuario$usuario"
