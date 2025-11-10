#ejer17
#Adivina el número (usar random).
import random
random_number = random.randint(1,10)
print("El numero aleatorio es: ",random_number)
number = int(input("Adivina el numero entre 1 y 10: "))
if number == random_number:
    print("Adivinaste el numero")
else:
    print("Fallaste!")