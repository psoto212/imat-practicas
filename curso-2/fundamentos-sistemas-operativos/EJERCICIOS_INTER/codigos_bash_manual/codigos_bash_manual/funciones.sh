#!bin/bash

inicio=2000
final=2022

mkdir calendarios

function busca_calendarios {
        find calendarios/ -name "*$1*"
}


for (( i=$inicio; i<$final; i++))
do
        cal $i > calendarios/calendario_"$i".txt
done

busca_calendarios "1"
