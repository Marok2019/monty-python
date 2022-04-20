from os import system
system("cls")

# calcular la división de dos números enteros positivos
# dados por el usuario y el resto

# entrada
dividend = int(input("Introduzca el dividendo: "))
divider = int(input("Introduzca el divisor: "))

# procesamiento (producto)
# iterador
quotient = 0

rest = dividend

while rest > 0:
    quotient += 1
    rest -= divider
    
# salida
print("El cociente es:", quotient)
print("El resto es: ", divider - rest)