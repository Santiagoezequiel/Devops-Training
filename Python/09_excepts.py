
"""
Try y Except son bloques de manejo de excepciones en Python
que se utilizan para manejar errores y excepciones que pueden
ocurrir durante la ejecucion de un programa
"""

try:
    #Bloque donde se pueden producir las excepciones
    #Si no hay excepciones, este bloque se ejecurará
    #Pueden ocurrir varias excepciones en un solo bloque
    pass
except:
    #Bloque para manejar las excepciones
    #Este bloque se ejecutará si ocurre
    pass
else:           # Opcional
    # Si no hay excepciones el codigo se ejecutará
    pass
finally:        # Opcional
    # No importa si el codigo tuvo errores o no
    # el codigo final siempre se ejecutará aquí.
    pass




#----------------------------------------------------


"""
Esto se utiliza para capturar tipos de errores especificos.
"""

try:
    pass
    # Se ejecutará si no ocurre ningun error
except ValueError:
    pass
    #Solo se ejecutará si hay un error de tipo ValueError.
except TypeError:
    pass
    #Solo se ejecutará si hay un error de tipo TypeError.



#---------------------------------------------------

"""
Con esto podemos almacenar el error en una variable "e"
o como queramos llamarla, y esta guardará todos los
detalles del error.
"""

try:
    parametro=int("abc")

except ValueError as e:
    print(f"Este es el error cometido en el try: {e}")





# Ejemplo de uso 

# entrada = input("Ingrese un numero ")

# try:
#     numero = int(entrada)
#     print("El numero ingresado es:",numero)
# except:
#     print(entrada ,"no es un numero valido")




"""
Las excepciones son errores que cortan el flujo de ejecucion,
cuando una excepcion ocurre el programa se puede detener
abruptamente.

Estos pueden ocurrir por diferentes maneras:

SyntaxError: Cuando hay algun error de sintaxis en el codigo.

ZeroDivisionError: Cuando se intenta dividir un numero por cero.

NameError: Cuando intentas acceder a una variable que no esta definida.

IndexError: Cuando intentas acceder a un indice fuera de rango(ej. en una lista).

TypeError: Cuando se intenta operar un tipo de dato que no es compatible (2 + "hola").

ValueError: Cuando recibe un argumento de tipo correcto pero con un valor incorrecto.

KeyError: Ocurre cuando intentas acceder a una key que no existe en el diccionario.

FileNotFoundError: Cuando intentas acceder a un archivo que no existe.

IOError: Cuando ocurre un error de E/S (ENtrada/Salida), como problemas al abrir, leer o escribir un archivo.

AttributeError: Cuando intentas acceder a un atributo que no existe en un objeto.

ImportError: Cuando ocurre un problema al importar un modulo.

KeyboardInterrupt: Ocurre cuando el usuario interrumpe la ejecucion con Cntrl + C.

MemoryError: Cuando no hay suficiente memoria para ejecutar una operacion.

OverflowError: Cuando un calculo aritmetico excede el rango permitido para el tipo de dato.

RecursionError: Cuando la profundidad maxima de recursion se excede.

StopIteration: Cuando la funcion next() de un iterador no tiene mas elementos para devolver.


"""    
