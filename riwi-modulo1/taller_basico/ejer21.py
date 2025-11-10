#ejer21
#Buscar un elemento en la lista
#Agregar y eliminar frutas.
fruit_list =["coco","curuba","pomo"]
#usamos .append() para agrear elementos a la lista
fruit_list.append("Guanabana")
#usamos .remove() para remover un elemento de la lista
fruit_list.remove("coco")
print(fruit_list)

#Buscar un elemento en la lista
 #Forma 1
if "Guanabana" in fruit_list:
    print(f"El elemento 'Guanabana' Existe.")
else:
    print("No existe")
#Forma 2
print("El elemento está en la posición:",fruit_list.index("Guanabana"))
