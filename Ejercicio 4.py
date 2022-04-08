# Escriba un programa que solicite al usuario ingresar una cantidad de dinero, y vaya
# mostrando el total acumulado. El programa termina una vez el usuario escribe un 0.

# entrada
money = int(input("Ingrese su cantidad de dinero: "))

# proceso
bank = 0

while money != 0:
    bank += money
    print("Total =", bank)
    money = int(input("Ingrese su cantidad de dinero: "))
    if money == 0:
        print("Hasta luego")
# salida