# Entradas
decimal = float(input("Introduzca un número: "))

# Procesamiento
rounded = int(decimal)
if decimal - rounded >= 0.5:
    rounded = rounded + 1
else:
    if decimal - rounded <= -0.5:
        rounded = rounded - 1

# Salidas
print("El número redondeado es: ", rounded)
