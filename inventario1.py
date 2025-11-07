nombre =input("Nombre producto: ")
#cantidad = int(input("Ingresa la cantidad: "))
while True:
    try:
        precio = float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Dato inválido, ingresa el numero nuevamente")
    
print(f"Valor del precio: {precio}") 