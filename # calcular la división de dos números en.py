# calcular la división de dos números enteros positivos
# dados por el usuario y el resto

# entrada
a = int(input("Introduzca el dividendo: "))
b = int(input("Introduzca el divisor: "))

# procesamiento (producto)
# iterador
cociente = 0

resto = a

while resto > 0:
    cociente += 1
    resto -= b
    
# salida
print("El cociente es:", cociente)
print("El resto es: ", b - resto)