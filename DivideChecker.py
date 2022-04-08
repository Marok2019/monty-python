from os import system
system("cls")

# Entradas
dividendo = int(input("Introduzca su dividendo: "))
divisor = int(input("Introduzca su divisor: "))
residuo = dividendo % divisor
cociente = dividendo / divisor

# Proceso
module = dividendo % divisor

# Salida
if residuo != 0:
    print(dividendo, "NO es divisible entre", divisor)
else:
    print(dividendo, "SI es divisible entre", divisor)
