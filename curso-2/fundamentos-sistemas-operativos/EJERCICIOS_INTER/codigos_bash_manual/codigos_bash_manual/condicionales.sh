#!/bin/bash

strings="prueba string cadena"
strings2="segunda string cadena"

for str1 in $strings
do
        for str2 in $strings2
        do
                if [ $str1 = $str2 ]; then
                        echo "$str1 es igual a $str2"
                else
                        echo "$str1 no es igual a $str2"
                fi

        done
done

numeros="2 3 4 5 6"
numeros2="3 4 5"

for num in $numeros
do
        for num2 in $numeros2
        do
                if [ $num -eq $num2 ]; then
                        echo "$num es igual a $num2"
                else
                        echo "$num no es igual a $num2"
                fi
        done
done
