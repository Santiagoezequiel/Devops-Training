def sumar(a, b):
    return a + b
    
def restar(a, b):
    return a - b
    
def multiplicar(a, b):
    return a * b
    
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"


def calculadora():
    print("Bienvenidos a la calculadora de Santi")
    print("Operaciones disponibles")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    
    operacion = input("Indique la operacion que desea realizar ")
    
    num1 = float(input("Ingrese primer valor "))
    num2 = float(input("Ingrese segundo valor "))

    
    
    if operacion == "1":
        print("Resultado: ", sumar(num1,num2))    
    elif operacion == "2":
        print("Resultado: ", restar(num1, num2))
    elif operacion == "3":
        print("Resultado: ", multiplicar(num1,num2))
    elif operacion == "4":
        print("Resultado: ", dividir(num1, num2))
    else:
        print("Opcion no valida")


calculadora()   