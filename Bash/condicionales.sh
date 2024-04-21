#! /bin/bash

numero=10


if (( numero = 10 )) 
then
echo "El numero es igual a 10 y uso la sintaxis diferente"

fi

numero2=11

if [ $numero2 -ne 10 ]
then
echo "El numero no es igual a 10"

fi

numero3=12

if [ $numero3 -gt 10 ]
then
echo "El numero es igual a 10"

fi

numero4=9

if [ $numero4 -lt 10 ]
then
echo "El numero es menor a 10"

fi

if [ $numero -ge 10 ]
then
echo "El numero es mayor o igual a 10"

fi



if [ $numero -le 10 ]
then
echo "El numero es menor o igual a 10"

fi



