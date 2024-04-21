#!/bin/bash

count=0

while (( $count <= 10 ))
do
    echo "Número: $count"
    ((count++))
done

echo "¡Fin del bucle!"
