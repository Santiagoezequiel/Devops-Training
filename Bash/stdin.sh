#! /bin/bash

echo "Lo que escribas aqui se transcribira al archivo.txt :"

while IFS= read -r line
do
echo "$line" >>  archivo.txt
done

