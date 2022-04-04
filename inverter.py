# entrada
org = int(input("Introduzca un número: "))

# proceso
x = org
inv = 0
digits = 0

while x > 0:
    d = x % 10
    inv *= 10
    inv += d
    x //= 10
    digits += 1

# salida
print("El número invertido es: ", inv)

print(inv, "tiene", digits, "dígitos.")

if inv == org:
    print("El número es capicúa.")
else:
    print("El número NO es capicúa.")
