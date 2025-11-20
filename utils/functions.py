
def miMenu():
    print("_______________________")
    print("        MENU           ")
    print("_______________________")
    print("1: Agrear producto     ")
    print("2: Mostrar producto    ")
    print("3: Calcular estadística")
    print("4: Salir               ")
    print("_______________________")
    print("") 
    
#Creacion de la función agregar libros al inventario en S3
def AddS3():
    c=0
    books=[]
    count_l=1
    while c <=5:
        print(f"-Agregando libros ({count_l})")
        count_l+=1
        book_title=input("Ingresa el nombre del libro: ")
#Agregamos un ciclo while para pedir al usuario multiples veces la información correcta, en caso de no hacerlo.
        while True:
            try:
                book_of_number = int(input("Ingresa la cantidad: "))
                break
            except ValueError:
                print("Dato inválido, ingresa la cantidad nuevamente")
        while True:
            try:
                book_of_price = float(input("Ingresa el  precio: "))
                break
            except ValueError:
                print("Dato inválido, ingresa el precio nuevamente")
    #Se crea un nuevo libro
        book={
            "title": book_title,
            "quantity":book_of_number,
            "price":book_of_price
        }
    #Se agrega el nuevo libro a la lista
        books.append(book)
        c+=1
        if c==5:    
            print("Deseas añadir un nuevo libro?  ")
            respuesta =input("Presione (S) para agregar o presione cualquier cosa para salir: ").lower()
            if respuesta =="s":
                c-=1  
            else:
                break
    return books

#Funcion para Consultar los libros disponibles en S3--------------------------------------------------------------------
def ConsultS3(global_books):
    if not global_books:
        print("No hay libros disponibles")
    else:
        for book in global_books:
            print(f"| Título: {book['title']} | Cantidad: {book['quantity']} | Precio: {book['price']:.2f} |")

    
#Funcion para actualizar el precio de un libro en S3 --------------------------------------------------------------------    
def UpdateS3(global_books):
    if not global_books:
        print("Aun no hay libros en el inventario")
    else:
        for i,book in enumerate(global_books):
            print(f"Item: {i+1}   | Título: {book['title']} | Cantidad: {book['quantity']} | Precio: {book['price']:.2f} |")
        print("")
        print("Ingresa el numero del item a actualizar: ")
            
        while True:
            try:
                item = int(input("Item: "))
                if item >0 and item<=len(global_books):
                    break
                else:print("Ingresa un item válido")
            except ValueError:
                print("Ingresa un item válido")
                
            
        while True:
            try:
                new_price =float(input("Ingresa el nuevo precio: "))
                if new_price >=0:
                    for i, books in enumerate(global_books):
                        i+=1
                        if item ==i:
                            books['price']=new_price
                            break
                    break
                else:
                    print("No se permiten numeros negativos")
            except ValueError:
                print("Entradas inválidas, Intenta nuevamente")
            
    #Imrprime directamente (Sin solicitarlo) el invetario actualizado.
        for i,book in enumerate(global_books):
            print(f"{i+1}  |- Título: {book['title']} | Cantidad: {book['quantity']} | Precio: {book['price']:.2f} |")
        
        


#Creo una función de borrado para S3
def DeleteS3(global_books):
    
    
    if not global_books:
        print("Aun no hay libros en el inventario")
    else:
        print("Item|        -- -- Inventario -- --")
        for i,book in enumerate(global_books):
                print(f" {i+1}  | Título: {book['title']} | Cantidad: {book['quantity']} | Precio: {book['price']:.2f} |")
        #Con While validamos que sea un numero válido
        print("")
        while True:
            try:
                
                remove_book = int(input("Que libro quieres eliminar? (Elige un numero): "))
                if remove_book >0 and remove_book<=len(global_books):
                    break
                else:print("Ingresa un item válido")
            except ValueError:
                print("Ingresa un item válido")
        libro_verificado=global_books[remove_book-1]
        if libro_verificado['quantity'] ==0 :
            print(f"No existen unidades de: {libro_verificado['title'] }")
            
        else:
            print(f"Aun existen unidades de {libro_verificado['title']}")
            delete = input("Eliminar de todos modos? (S/-) :").lower()
            if delete =="s":
                global_books.pop(remove_book-1)
                print(f"Eliminaste el libro: {libro_verificado['title']}")

        print("\n--- DEBUG: Contenido de global_books al salir de DeleteS3 ---")
        for book in global_books:
            print(f"DEBUG: {book['title']}")
        print("----------------------------------------------------------\n")



#creamos un menú en una función para S3 ------------------------------------------------------------------------------
def MenuS3():
    print("___________________________________")
    print("_______________MENU________________")
    print("1: Añadir libros al inventario.")
    print("2: Consultar libros en inventario.")
    print("3: Actualizar precios de libros.")
    print("4: Eliminar libros del inventario.")
    print("5: Calcular valor total.")
    print("6: Salir.")
    print("___________________________________")
    print("")

