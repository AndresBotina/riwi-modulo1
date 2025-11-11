#ejer12
#Comparador de tres números: mayor y menor.
number = int(input("Ingresa un numero: "))
number2 = int(input("Segundo numero: "))
number3 = int(input("Tercer numero: "))

if number < number3 and number2<number3:
    print(f"El mayor es {number3}")
elif number < number2:
    print(f"El mayo es {number2}")
else:
    print(f"El mayor es {number}")