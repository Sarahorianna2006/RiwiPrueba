#Acceso exclusivo al evento

edad = int(input("Ingresa tu edad: "))
invitacion = (input("Ingresa el numero de tu invitacion: "))

if edad > 21 and invitacion == "777":

    print("puede ingresar")
else:
    print("No puede ingresar")


    #Mayor de edad (sin condicional)
edad = int(input("Ingrese su edad: "))

print("Usted es mayor de edad"), edad >=18


#Descuento por edad o monto

compra = int(input("Ingresa el valor total de la compra: "))
edad = int(input("Ingrese su edad: "))

if compra > 100 or edad > 60:
    print("usted tiene un descuento en esta compra")
else: 
    print("usted no tiene un descuento")


    #Mayor de edad (sin condicional)
edad = int(input("Ingrese su edad: "))
print("¿Usted es mayor de edad?\n>",edad >=18)


#Verificación para participar en un concurso internacional

edad = int(input("Ingrese su edad: "))
pais = input("Ingrese el pais donde nacio: ").lower()
documento = int(input("Ingrese su numero de documento: "))

#if edad >=18 and edad <= 30 and pais != "antartida" and documento != 0:
if 18<= edad <=30 and pais != "antartida" and documento!=0:
    print("Cumple las condiciones, puedes participar en el concurso")
else: 
    print("No cumple las condiciones")
