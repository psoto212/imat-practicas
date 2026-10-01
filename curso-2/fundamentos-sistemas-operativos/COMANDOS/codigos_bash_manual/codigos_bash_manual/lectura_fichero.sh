#!bin/bash

fichero_leer="fichero.txt"
c=1
while read -r linea
 do
  echo "Linea $c. Contenido: $linea"
  let c++

done < "$fichero_leer"
