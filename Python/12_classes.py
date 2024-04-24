#### Clases ####

"""
Las clases se deben definir con CamelCase
"""

# Creamos la clase
class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
    def walk (self):
        print(f"{self.name} {self.surname} el {self.alias} Está caminando")

# __init__ es el constructor de la clase y es obligatorio
# tanto como el uso de self, y siempre debe ser el primer parametro
# este llama a la clase en si misma.

# Creamos la instancia de la clase
my_person = Person("Santiago", "Castaño")

# Con la instancia podremos llamar a las funciones
# dentro de la clase, con la sintaxis instancia.funcion()


my_person.walk()        # Al llamar a las instancias el self se indica implicitamente
#                         Osea no es necesrio indicarla dentro de los ()

#Creamos otra instancia de la clase

my_person_two = Person("Juan", "Cristobal", "Papucho")
my_person_two.walk()

class Person2:
    def __init__(self, name):
        self.__name = name  # Esto crea una propiedad privada y no podemos acceder a ella
        