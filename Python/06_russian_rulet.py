"""
Tomando la logica aprendida hasta el momento, decidi diseñar este sencillo
codigo con dos elementos: Vida y Muerte.

Ya que los sets en cada ejecucion cambian su orden, al pasarlo al tipo
lista, puedo seleccionar sus elementos segun su indice, pero tomando en cuenta
lo anterior, los elementos nunca estaran en la misma posicion.

Por lo que deja una probabilidad de 50 / 50.

Entiendo que hay maneras mas efectivas de crear un prototipo como este
(por ej con condicionales y funciones) pero decidi crearlo con los conocimientos
que adquiri actualmente.

Proximamente lo remasterizaré haciendolo mas optimo.
"""


sets = {"Vida", "Muerte"}

lista = list(sets)

print(lista[0])