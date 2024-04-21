#!/bin/bash

contador=0

until (( $contador == 5 )); do
  echo "El contador es $contador"
  contador=$((contador + 1))
done

echo "Bucle terminado"
