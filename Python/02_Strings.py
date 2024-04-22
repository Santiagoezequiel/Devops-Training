
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
a, b, c, d, e, f = language     #Separa cada caracter del str y lo almacena en diferentes variables

# print(a)
# print(b)                    # !DEBE COINCIDIR LA CANTIDAD DE CARACTERES CON LA CANTIDAD DE VARIABLES
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



print(palabra.capitalize())                    #COnvierte la primera letra del str en MAY
print(palabra.upper())                         #Convierte el str en MAY
print(palabra.count("e"))                      #Cuenta la cantidad de veces que se repite la "e"
print(palabra.isnumeric())                     #Verifica si el valor es un numero (En este caso es FALSE)
print(palabra.lower())                         #Convierte el str en MIN
print(palabra.lower().islower())               #Lo convierte en MIN y luego verifica si lo está
print(palabra.endswith("eo"))                  #Verifica si el str termina en "eo"
print(palabra.startswith("es"))                #Verifica si el str comienza con "es"
print(palabra.title())                         #Pone en MAY la primer letra de cada palabra


