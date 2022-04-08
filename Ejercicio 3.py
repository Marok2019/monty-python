# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo
# el segundo número mientras no sea mayor que el primero. El programa terminará
# escribiendo los dos números

from os import system
system("cls")

# entradas
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca un número: "))

# proceso
while num2 <= num1:
    print(num2, "NO es mayor que", num1, "|", "Inténtalo de nuevo:")
    num2 = int(input("Introduzca un número: "))

# salida
if num2 > num1:
    print("Los números que ha introducido son", num1, "y", num2, ".")