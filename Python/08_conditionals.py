#### CONDICIONALES ####



my_condition = True

if my_condition:                    #Luego del punto y con la tabulacion se  indica la accion del if.
    print("Ejecucion del if")
#                                   Para salir del if dejamos un espacio de linea y le sacamos el Tab.
print("----------------------")


condition1 = 10 * 3

if condition1 >= 10 and condition1 <= 20 :
    print("Puntaje valido")
else:
    print("Puntaje invalido")
    
    
print("----------------------")
    
    
    
if isinstance(condition1, str):
    print("Puntaje valido:", condition1)
else:
    print("Esto no es un texto")


print("----------------------")


vacio = ""

if vacio:
    print("La variable no esta vacia")
else:
    print("La variable no contiene ningun dato")
    
#################################################
if not vacio:
    print("La variable contiene datos")                 #Al negar a la variable invertimos su valor
else:                                                   #Como antes daba False ahora da True
    print("La variable no contiene ningun dato")
    

