


diccionario = {
    "Nombre":"Santiago",
    "Apellido":"Castaño",
    "Edad":22,
    "Lenguajes":{"Python", "Js", "C#"},
    "Monto":100,
    "Total":300,
    "Gastos":200
    }

print(len(diccionario))

diccionario["Direccion"] = "Jean Jaures"

print(diccionario)

dic_vacio = dict.fromkeys(diccionario)

print(dic_vacio)



