### FUNCIONES ###

def mi_funcion():                           # DEF para definir la funcion.
    print("Esto es una funcion")
    
mi_funcion()                                # Nombre de la funcion() para ejecutarla.


#-----------------------------------------------------

def sumar(primer_num, segundo_num):
    print(primer_num + segundo_num)
    

sumar(3,1)

#-----------------------------------------------------

"""
Al llamar a la variable se ejecutan sus acciones pero luego
de que termina no devuelve ningun valor a la linea de ejecucion.
Si queremos que la funcion devuelva un valor devemos usar
la palabra reservada RETURN
"""


def sumar_y_retornar(primer_valor, segundo_valor):
    return primer_valor + segundo_valor


resultado = sumar_y_retornar(10,5)

print(resultado)

"""
El valor que retorne se debe guardar en una variable o
directamente dentro del print para mostrarlo por consola.
"""
# Primero pedimos name, y luego surname
def print_name(name, surname):
    
    print(f"{name} {surname}")
    
#         Lammamos primero a surname y luego a name
print_name(surname = "Castaño", name = "Santiago")

"""
Aunque al definir la funcion primero se pedia el name y luego surname
al llamarla puedo cambiar el orden a gusto pero asignando cada 
valor a su correspondiente parametro.
"""


def param_default(nombre, apellido, alias = "Sin alias"):
    print(f"{nombre} {apellido} {alias}")
    

param_default("Santiago", "Castaño")

"""
Los parametros por defectos ayudan cuando necesitamos ingresar
menos valores que la cantidad de parametros, y que este no nos de un error.
 
"""

def infinit_params(*parametros):
    print(parametros)

infinit_params("Hola", "Soy", "Una", "Funcion", "Con", "Parametro", "Infinitos")
"""
Funciones con parametros arbitrarios
"""

def funct_params(*parametros):
    for param in parametros:
        print(param.upper())
        
        
funct_params("Hola", "Soy", "Una", "Funcion", "Con", "Parametro", "Infinitos", "y", "Arbitrarios")       
        












