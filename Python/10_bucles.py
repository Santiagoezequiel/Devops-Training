#### BUCLES ####


## While

numero = 0

while numero <= 10:
    print(numero)
    numero += 1

print("Se ha detenido el bucle")


"""
A difernecia de otros lenguajes de programacion
en Python podemos agregarle un else al bucle 
"""
while numero <= 10:
    print(numero)
    numero += 1
else:
    print("Mi condicion es mayor o igual a 10")
    
    
    
"""
Investigar recursividad
"""

condicion=0

while condicion <= 10:
    print(condicion)
    condicion += 1
    if condicion == 5:
        print("La ejecucion es 5, deteniendo ejecucion...")
        break
    
    
########################## FOR #################################################

lista = [1, 2, 3, 4, 5, 6, 7, 8]


for element in lista:
    print(element)
    

"""
Aparte del BREAK tambien existe el continue, que hace un salto de linea y
vuelve al for para seguir con la siguiente iteracion. Esto no es muy 
aconsejable por que al dia de hoy existen mejores soluciones.
"""
    
    
    