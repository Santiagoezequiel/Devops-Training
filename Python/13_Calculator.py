def sumar(num1, num2):
    print(num1 + num2)
    
def restar(num1, num2):
    print(num1 - num2)
    
def multiplicar(num1, num2):
    print(num1 * num2)
    
def dividir(num1, num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print("No se puede dividir entre 0")


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
        sumar(int(num1), int(num2))    
    elif operacion == "2":
        restar(int(num1), int(num2))
    elif operacion == "3":
        multiplicar(int(num1), int(num2))
    elif operacion == "4":
        sumar(int(num1), int(num2))
    else:
        print("Elija una opcion valida")
        print("")
        calculadora()


calculadora()   