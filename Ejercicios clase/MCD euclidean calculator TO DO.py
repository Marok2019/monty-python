from os import system
system("cls")

# entradas
num1 = int(input("Introduzca valor A: "))
num2 = int(input("Introduzca valor B: "))

# proceso
mcd = 1
divisor = 2

if num1 > num2:
    greater = num1
    lesser = num2
else:
    greater = num2
    lesser = num1

if num1 % num2 == 0:
    mcd = lesser
else:
    resto = lesser / (num1 % num2)
    
    if resto - int(resto) == 0:
        mcd = resto
    else:



# salida
print("El MCD entre", num1, "y", num2, "es", mcd)