### Modulos ###

"""
Se utilizan para poder importar y exportar codigo
desde diferentes ficheros.
Por ejemplo, si queremos usar una funcion del 
fichero mi_modulo, en vez de transcribir
toda la funcion, podemos importarla
"""

# Caaso 1: Si queremos importar un fichero de otro directorio
import Modulos.mi_modulo as mi_modulo

# Caso 2: Si queremos importar una funcion especifica y no todo el fichero
from Modulos.mi_modulo_dos import exo
from Modulos.mi_modulo import sumita

# Asi las debemos llamar en el Caso 1
mi_modulo.imprimir("Holiiiii")


# Asi las debemos llamas en el Caso 2
exo("Esta es una funcion de otro directorio")
sumita(3, 5)

# Tambien podemos usar modulos predefinidos como math
import math

# Esto imprimirá el numero pi.
print(math.pi)
# Esto imprimirá 2 elevado a la 8.
print(math.pow(2,8))