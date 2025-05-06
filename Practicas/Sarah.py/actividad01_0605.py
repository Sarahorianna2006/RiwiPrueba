#Nombre y edad.

nombre = input("Escribe tu nombre: ")
edad= int(input("Escribe tu edad: "))
print(f"Hola {nombre}, tienes {edad} años!")


#Suma de dos números enteros

numero1 = int(input("Ingresa el primer numero a sumar: "))
numero2 = int(input("Ingresa el segundo numero a sumar: "))

suma = numero1 + numero2
print(f"El resultado de la suma es: {suma}")


#Multiplicacion de decimales

numero1 = float(input("Ingresa el primer número a multiplicar: "))
numero2 = float(input("Ingresa el segundo número a multiplicar: "))

multiplicacion = numero1 * numero2

print(f"El resultado de la multiplicacion es: {multiplicacion}")


#Doble y triple

numero1 = int(input("Escribe el numero a consultar: "))

calculo1 = numero1 * 2
calculo2 = numero1 * 3

print(f"El doble del número es {calculo1} y el triple del número es {calculo2}")


#Repetir palabra

palabra = input("Escribe una palabra:\n> ")
numero1 = int(input("Escribe el número de veces que deseas repetir la palabra:\n> "))

print(f"{(palabra + "\n") * numero1}") 


#División

numero1 = int(input("Escribe el primer número a dividir: "))
numero2 = int(input("Escribe el segundo número a dividir: "))

division = numero1 / numero2

print(f"El resultado de la división es: {division}")


#Letras del nombre

nombre = input("¿Cúal es tu nombre?\n>")
letras = len(nombre)

print (f"Tú nombre tiene {letras} letras")


#División entera y módulo

numero1 = int(input("Escribe el primer número a dividir: "))
numero2 = int(input("Escribe el segundo número a dividir: "))

division = numero1 // numero2 
modulo = numero1 % numero2

print(f"El resultado de la división es: {division} y su módulo es: {modulo} ")


#Todas las operaciones

numero1 = int(input("Escribe el primer número a consultar: "))
numero2 = int(input("Escribe el segundo número a consultar: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"El resultado de la suma es {suma}, de las resta es {resta}, de la multiplicación es {multiplicacion} y la division es {division} ")
#print(f"Los resultados entre ambos numeros es:\n Suma: {suma}\n Resta: {resta}\n Multiplicación: {multiplicacion}\n Division: {division} ")
#Respuesta fuera de lo pedido, pero la agregue como un adicional, ya que seria una mejor respuesta.


#Potencias con f-strings

numero1 = int(input("Ingresa el número entero: "))

print (f"El {numero1} al cuadrado es: {numero1 ** 2}")
print (f"El {numero1} al cubo es: {numero1 ** 3}")


#Parte entera de un decimal

numero = float(input("Ingrese un número decimal: "))
input(f"El número ingresado, como entero seria: {numero:.3f}")


