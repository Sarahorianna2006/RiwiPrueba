edad = int(input("Cual es tu edad? "))

if edad >= 0 and edad < 18:
    print("Eres menor de edad.")
elif edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Edad incorrecta")

operacion = edad % 2

if operacion == 0:
    print("la edad es par")
else:
    print("la edad es impar")
    

# Colecciones de datos
    # conjunto de datos 
lista = [1,2,3,"camila", True, False]

tupla = (2, False, "Carro", 3.121234)

diccionario = {"Nombre":"Carolina", "Apellido":"Perez", "Edad":18, "Mayor_edad": True}