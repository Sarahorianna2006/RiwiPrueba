#Activida de desarrollo 3

inventory = {
    "lapiz" :(2, 5 ),
    "perfume" :(5, 2),
    }

#productos = []


def añadir_producto(): 
    nombre = input("Ingresa el nombre del produlto:\n>")
    precio = int(input("Ingresa precio del producto:\n>"))
    cantidad= int(input("Ingresa la cantidad del producto:\n>"))

    #invent_dict ={
    #"nombre_prod": nombre,
    #"precio_prod": precio,
    #"cant_prod" : cantidad 
    #}
    
    #productos.append(invent_dict)

    inventory[nombre] = (precio, cantidad)
    #inventory/añadir = 


print(inventory)
añadir_producto()
print(inventory)

def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desee buscar:\n>")
    exist_product = inventory.get(nombre) # (2, 5) | (precio, cantidad)
    if exist_product:
        print("el precio es:\n>", exist_product[0])
        print("la cantidad es:\n>", exist_product[1])
    else:
        print("El producto consultado; no existe.\n> Verifique nuevamente.")

buscar_producto()



