def MenuHU3():
    print("___________________________________")
    print("_______________MENU________________")
    print("1: Agregar")
    print("2: Mostrar")
    print("3: Buscar")
    print("4: Actualizar")
    print("5: Eliminar")
    print("6: Estadísticas")
    print("7: Guardar CSV")
    print("8: Cargar CSV")
    print("9: Salir")
    print("___________________________________")
    print("")

def agregar_productoHU3():
    respuesta=1
    productos=[]
    count_p=1
    while respuesta!=0:
        print(f"Producto {count_p}:")
        count_p+=1
        nombre_producto=input("Ingresa el nombre del producto: ")
#Agregamos un ciclo while para pedir al usuario multiples veces la información correcta, en caso de no hacerlo.
        while True:
            try:
                cantidad_del_producto = int(input("Ingresa la cantidad: "))
                break
            except ValueError:
                print("Dato inválido, ingresa la cantidad nuevamente")
        while True:
            try:
                precio_del_producto = float(input("Ingresa el  precio: "))
                break
            except ValueError:
                print("Dato inválido, ingresa el precio nuevamente")
    #Se crea un nuevo producto
        producto={
            "name_product": nombre_producto,
            "quantity":cantidad_del_producto,
            "price":precio_del_producto
        }
    #Se agrega el nuevo producto a la lista
        productos.append(producto)
        respuesta =input("Presione (S) para agregar o presione cualquier cosa para ir a Menú: ").lower()
        if respuesta =="s":
            continue
        else:
            respuesta =0
    return productos

#Creo una lista para mostrar los productos creados:

def mostrar_productoHU3(inventario_globalHU3):
    #product = input("INgrese ")
    if not inventario_globalHU3:
        print("No hay productos en el inventario")
    else:
        for producto in inventario_globalHU3:
            print(f"| Título: {producto['name_product']} | Cantidad: {producto['quantity']} | Precio: {producto['price']:.2f} |")

def buscar_productoHU3(inventario_globalHU3):
    print("")
    buscar = input("Que producto quieres buscar: ")
    for producto in inventario_globalHU3:
        if buscar ==producto["name_product"]:
            print(producto)
            return
    print("No encontrado")