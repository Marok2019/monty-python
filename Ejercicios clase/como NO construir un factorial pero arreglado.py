from os import system
system("cls")

# entrada
num1 = int(input("Introduzca un número: "))

# proceso

# definiciones
fact = num1
i = num1

# ciclo
while i > 1:
	i -= 1
	fact *= i

# salida
print("El factorial de", num1, "es:", fact)