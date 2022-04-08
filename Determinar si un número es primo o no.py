from os import system
system("cls")

# Determinar si un número es primo o no

# Entrada
num = float(input("Introduzca su número: "))
# Proceso
i = 1
times_divided_exactly = 0
while i <= num:
    cociente = num / i
    i += 1
    if cociente - int(cociente) == 0:
        times_divided_exactly += 1

# Salida
if times_divided_exactly == 2:
    print(num, "SÍ es un número primo.")
else:
    print(num, "NO es un número primo.")