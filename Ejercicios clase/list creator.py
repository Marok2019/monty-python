from os import system
system("cls")

# Crear un programa que permita ver la lista de números enteros desde A hasta B 
# ingresados por el usuario, validando que A sea menor a B. 

# entrada
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

# proceso
while num1 <= num2:

# salida
    print(num1)
    num1 += 1