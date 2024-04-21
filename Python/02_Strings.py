
################### Concatenacion en STRINGS #####################


name, surname, age = "Santiago", "Castaño", 33

### Manera N1 ###

print(f"Yo {name} {surname} tengo {age} años")

### Manera N2 ###

print("Mi nombre es %s y tengo %d años." %(name,age))

### Manera N3 ###

print("Mi nombre es {} y tengo {} años.".format(name,age))


################# Desempaquetado de caracteres ###################

language = "Python"
a, b, c, d, e, f = language

# print(a)
# print(b)
# print(c)


slice = language[1:5]

print(slice)

##########################

slice_dos = language[0:]

print(slice_dos)

##########################

slice_tres = language[-1]

print(slice_tres)

##########################


reversed = language[::-1]

print(reversed)

##########################

palabra = "ABCDEFGHIJKLMNOPQ"

jumped = palabra[0:17:2]

print(jumped)

##########################

############ Metodos de Strings ##################

palabra = "esternocleidomastoideo"



print(palabra.capitalize())
print(palabra.upper())
print(palabra.count("e"))
print(palabra.isnumeric())
print(palabra.lower())
print(palabra.lower().islower())
print(palabra.endswith("eo"))
print(palabra.startswith("es"))