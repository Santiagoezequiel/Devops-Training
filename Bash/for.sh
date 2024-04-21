#! /bin/bash

#for file in $(ls *.sh)
#do(
#    echo $file
#done


for ((i= 0; i<10; i++))
do
    
    echo $i
    if [ $i -eq 5 ]
    then
    break
    fi
    
done



#echo "Los argumentos pasados son:"
#for i in "$@"
#do
#    echo "- $i"
#done
