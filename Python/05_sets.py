"""
Los sets se basan en una estructura desordenada llamada
HASH TABLE o HASH MAP
"""



mi_set = {5, 1, 2.9, 2, "pepe", 3, 4}

print(mi_set)

mi_set.add(34)

print(mi_set)

print("Pepe" in mi_set)     #Comprueba si esta este elemento en el set





mi_set.remove(2.9)        #Elimina el elemento identificado

print(mi_set)

# mi_set.clear()              #Vacia el set al igual que las listas

# print(mi_set)

# del mi_set                  #Como todos los demas objetos, se puede eliminar


set = {"Santiago", "Dev", "Ops"}
set1 = {"Castaño", "Front", "end"}

completo = set.union(set1)

print(completo)

# print(completo.union(set))        #Esto no funcionará ya que set no acepta repetidos

completo.discard("Dev")             #ESto elimina un elemento al igual que remove, pero si no lo encuentra no hara nada.
print(completo)


