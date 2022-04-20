from os import system
system("cls")

# entrada
num = int(input("Introduzca un número: "))

# proceso
x = num
digits = 0

while x > 0:
    digits =+ 1
    
    num *= 10
    num += x
    x //= 10
    
# salida
print(num, "tiene", digits, "dígitos.")
