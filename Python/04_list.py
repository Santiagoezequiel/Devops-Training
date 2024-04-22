my_list = list([2, 3, 4, 5, 6, 6, "destino"])
my_other_list = []



print(len(my_list))
print(type(my_other_list))


print(my_list[-1])
print(my_list[len(my_list) - 1])

lista = [2, 3, 5, 12, 3, "Hola"]

lista.pop()

print(lista.pop())
print(lista)

variable = lista.pop()
print(variable)

lista.sort()    ##Esto dará un error ya que no soporta str e int en la misma lista

sub_lista = lista[1:5]

print(lista)
print(sub_lista)



################################### TUPLAS #####################################

mi_tuple= tuple((1, 2, 3, 4))
print(mi_tuple)

mi_tuple = list(mi_tuple)

print(type(mi_tuple))

mi_tuple[1] = "Dos"
mi_tuple.insert(2, "Tres")

mi_tuple = tuple(mi_tuple)

print(mi_tuple)
print(type(mi_tuple))
