#Creo una función Menú
def miMenu():
    print(" _______________________")
    print("|        MENU           |")
    print("|_______________________|")
    print("|1: Agrear producto     |")
    print("|2: Mostrar producto    |")
    print("|3: Calcular estadística|")
    print("|4: Salir               |")
    print("|_______________________|")
    print("")

miMenu() 
#Solicitamos al usuario lo que desea hacer
menu =0
print("")
#Creo una nueva lista
inventario = []
#contador
cantidad_total = 0
precio_total = 0
sumatoria = 0
costo_total = 0
precio_final = 0
#Creo un diccionario
while menu!=4:
    
    try:
        menu = int(input("¿Que quieres hacer?: "))
        print("")
        #Uso un condicional para agregar producto
        if menu ==1:
            
            print("----AGREGANDO PRODUCTOS----")
            #Creo un diccionario
            product = {
            }
            product_name = input("Ingresa el nombre del producto: ")
            product["Name product"] = product_name
            product_amount = int(input("Ingrese la cantidad del producto: "))
            product["Product amount"] = product_amount

            product_price = int(input("Ingrese el precio del producto: "))
            
            product["Product price"] = product_price

            precio_total = product_amount*product_price
            cantidad_total +=product_amount
            precio_final+=precio_total
            #Agrego el dicionario a una lista llamada producto
            inventario.append(product)
            print("")

        elif menu==2:
            if not inventario:
                print("----La lista está vacía!----")
            else:
                for producto in inventario:
                    print(producto)
            print("")
        elif menu==3:
            
            print(f"La cantidad de productos registrados es: {cantidad_total}")
            print("")
            print(f"El precio total es: {precio_final}")
        elif menu==4:
            print("¡Has salido!")
            break
        else:
            print("**** Has elegido una opción invalida ****")
            print("")
        miMenu()
            
        print("") 
    except ValueError:
        print("")
        print("**** Entradas inválidas **** ")
        print("")
        miMenu()