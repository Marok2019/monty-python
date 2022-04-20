from os import system
system("cls")

# entrada
number = float(input("Introduzca un número: "))

# proceso
decimal = 0
integer = 0
positive = 0
negative = 0

while number != 0:


# cajón decimal/entero
    rational = number - int(number)
    if rational != 0:
        decimal += 1
    else:
        integer += 1

# cajón positivo/negativo
    z_plus_0 = number
    if z_plus_0 > 0:
        positive += 1
    else:
        negative += 1

    number = float(input("Introduzca un número: "))

# salida
    if number == 0:
        print("Hay", decimal, "números decimales.")
        print("Hay", integer, "números enteros.")
        print("Hay", positive, "números positivos.")
        print("Hay", negative, "números negativos.")