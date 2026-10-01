#!/bin/bash

echo "while"
contador=0
while [ $contador -lt 4 ]; do
    let contador+=1
    echo $contador
done

echo "until"
contador=6
until [ $contador -lt 4 ]; do
    let contador-=1
    echo $contador
done
