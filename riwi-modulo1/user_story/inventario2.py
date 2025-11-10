def miMenu():
    print("MENU")
    print("1: Agrear producto")
    print("2: Mostrar producto")
    print("3: Calcular estadística")
    print("4: Salir")
    print("")



miMenu() 
#Solicitamos al usuario lo que desea hacer
menu = int(input("Que deseas realizar?: "))
print("")
#Creo una nueva lista
inventario = []
#contador
cantidad_total = 0
precio_total = 0
sumatoria = 0
costo_total = 0
#Creo un diccionario
while menu>0:
    #Uso un condicional para agregar producto
    if menu ==1:
        
        print("***************AGREGANDO PRODUCTOS******************")
        #Creo un diccionario
        product = {

        }
        product_name = input("Ingresa el nombre del producto: ")
        product["Name product"] = product_name
        product_price = float(input("Ingrese el precio del producto: "))
        product["Product price"] = product_price
        precio_total+=product_price
        product_amount = int(input("Ingrese la cantidad del producto: "))
        product["Product amount"] = product_amount
        cantidad_total +=product_amount
        #Agrego el dicionario a una lista llamada producto
        inventario.append(product)
        print("")
        #CANTIDAD DE PRODUCTOS
        #cantidad_productos = cantidad_productos +1

    elif menu==2:
        if not inventario:
            print("La lista está vacía!")
        else:
          for producto in inventario:
            print(producto)
        print("")
        
    elif menu==3:
        
        print("La cantidad de productos registrados es: ",cantidad_total)
        break
    elif menu==4:
        print("¡Has salido!")
        break
    else:
        print("Opción invalida.")
        print("")
    miMenu()
        

    menu=int(input("Que desea realizar?: "))
    print("") 
