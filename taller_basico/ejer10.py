#ejer10
#Calculadora básica con +, -, *, /.
number = float(input("Ingresa un numero para calcular: "))
number2 = float(input("Ingresa el segundo numero para calcular: "))
operator = input("Que operación desea hacer,  + - * / : ")
if operator =="+":
    print(f"La operación es {number}{operator}{number2} = {number+number2} ")
elif operator=="-":
    print(f"La operación es {number}{operator}{number2} = {number-number2} ")
elif operator=="*":
    print(f"La operación es {number}{operator}{number2} = {number*number2} ")
elif operator=="/":
     print(f"La operación es {number}{operator}{number2} = {number/number2} ")
    
    
    