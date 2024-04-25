/*
Go no es un lenguanje orientado a objetos. Por lo tanto
no existen las clases ni los objetos.
Es un lenguaje con tipado fuerte.
*/

package main

import (
	"container/list"
	"fmt" //	Paquete de formateo
	"reflect"
)

func main() {
	fmt.Println("Hola mundo") // Print con salto de linea
	// fmt.Printf("Hola mundo")			// Print con formateo de string
	// fmt.Print("Hola mundo")			// Print comun y corriente

	//		Siempre que se defina una variable se tiene que asignar
	//		No pueden existir variables vacias.
	var myString string = "Esto es una cadena de texto"
	fmt.Println(myString)

	//	myString = 6 Error		Una variable de tipo str sera str hasta que se muera

	//	Integers
	var myInt = 7 //	Los Int se pueden definir con los bits que deseas que ocupen.
	myInt += 3    //	Mientras mayor sean los bits mas espacio en la memoria ocupará.
	fmt.Println(myInt)
	fmt.Println(myInt - 1)
	fmt.Println(myInt + 5)

	fmt.Println(myString, myInt)

	var myFloat = 5.4

	fmt.Println(reflect.TypeOf(myInt))
	fmt.Println(reflect.TypeOf(myFloat))

	fmt.Println(myFloat + float64(myInt))

	var myBool = false
	myBool = true
	fmt.Println(myBool)

	//	Variable definida de manera resumida
	myStrong := "Esto es otra cadena"
	fmt.Println(myStrong)

	// Constantes

	const myConst = "Miconstante" // Las constante se pueden definir y no usarlas y no dará error.

	// 	Control de flujo

	myInt = 12

	if myInt == 10 {
		fmt.Println("Mi valor es igual a 10")
	} else if myInt == 11 {
		fmt.Println("Mi valor es igual a 11")
	} else {
		fmt.Println("El valor no es 10 ni 11")
	}
	/*********************************************/

	myStrong = "Hola"

	if myInt == 10 && myStrong == "Hola" { // OPERADORES LOGICOS
		fmt.Println("Mi valor es igual a 10")
	} else if myInt == 11 || myInt == 12 {
		fmt.Println("Mi valor es igual a 11")
	} else {
		fmt.Println("El valor no es 10 ni 11")
	}

	/*********************************************/

	// ARRAYS

	var myArray [3]int
	myArray[0] = 1
	myArray[1] = 2
	myArray[2] = 3

	fmt.Println(myArray)

	var myArray2 [3]string
	fmt.Println(myArray2)

	// MAP

	myMap := make(map[string]int)
	myMap["Santi"] = 22
	myMap["Carla"] = 20
	fmt.Println(myMap)

	// Manera resumida
	myMap2 := (map[string]int{"Santiago": 23, "Carlita": 21})
	fmt.Println(myMap2)

	// Lista

	myList := list.New()
	myList.PushBack(1)
	myList.PushBack(2)
	myList.PushBack(3)
	fmt.Println(myList.Back().Value)

	// Bucles

	for index := 0; index < len(myArray); index++ {
		fmt.Println(myArray[index])
	}

	for index, value := range myArray {
		fmt.Println(index, value)
	}

	// Funciones

	fmt.Println(myFunctions())

	// Estructura

	type myStruct struct {
		name string
		age  int
	}

	Estructura := myStruct{"Santiago", 22}
	fmt.Println(Estructura)
}

func myFunctions() string {
	return "Mi funcion"
}
