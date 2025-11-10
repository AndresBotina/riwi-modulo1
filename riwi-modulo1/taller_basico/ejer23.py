#ejer23
#Números pares: guardar solo los pares.
pars = []
pares = int(input("Ingresa numeros y nosotros separamos los pares: "))
while pares!=0:
    
    if pares%2 ==0:
        pars.append(pares)
     
    pares = int(input("Ingresa numeros y nosotros separamos los pares, o presiona 0(Cero) para salir : "))
    
    
print(f"Mi lista de pares: {pars}")