"""
Try y Except son bloques de manejo de excepciones en Python
que se utilizan para manejar errores y excepciones que pueden
ocurrir durante la ejecucion de un programa
"""

try:
    #Bloque donde se pueden producir las excepciones
    #Si no hay excepciones, este bloque se ejecurará
    #Pueden ocurrir varias excepciones en un solo bloque
    print()
except:
    #Bloque para manejar las excepciones
    #Este bloque se ejecutará si ocurre
    print()


entrada = input("Ingrese un numero ")

try:
    numero = int(entrada)
    print("El numero ingresado es:",numero)
except:
    print(entrada ,"no es un numero valido")


"""
Las excepciones son errores que cortan el flujo de ejecucion,
cuando una excepcion ocurre el programa se puede detener
abruptamente.

Estos pueden ocurrir por diferentes maneras:

SyntaxError: Cuando hay algun error de sintaxis en el codigo.

ZeroDivisionError: Cuando se intenta dividir un numero por cero.

NameError: Cuando intentas acceder a una variable que no esta definida.

IndexError: Cuando intentas acceder a un indice fuera de rango(ej. en una lista)

TypeError: Cuando se intenta operar un tipo de dato que no es compatible (2 + "hola")


"""    