#! /bin/bash

echo "Escoge entre el valor 1 o 2"
read valor

case $valor in
1)
echo "Elegiste el numero 1"
;;
2)
echo "Elegiste el numero 2"
;;
*)
echo "Valor invalido"
;;
esac