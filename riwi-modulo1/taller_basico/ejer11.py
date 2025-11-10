#ejer11
#Clasificador de notas (Excelente, Aprobado, Reprobado).
calificacion = float(input("Ingresa la calificación: "))

if calificacion >=0 and calificacion<=5:
    if calificacion>=4.5 and calificacion <=5:
        print("Excelente.")
    elif calificacion >= 3.0 and calificacion<=4.4:
        print("Aprobado")
    elif calificacion<=2.9:
        print("Reprobado")
else:
    print("Ingresaste un dato inválido")