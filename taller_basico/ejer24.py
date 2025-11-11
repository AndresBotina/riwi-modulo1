#ejer24
#Eliminar duplicados

my_list = [1,2,3,3,4,5,7,2,35,5,"hola,",4,7,9,10,11,4]
no_repeated=[]
repeated =[]
for element in my_list:
    if element not in no_repeated:
        no_repeated.append(element)
    else:
        repeated.append(element)
print(f"Lista original: {my_list}")
print(f"Lista de no repetidos: {no_repeated}")
print(f"Lista de repetidos: {repeated}")