from os import system
system("cls")

# entrada
year = int(input("Introduzca un año: "))

# proceso
a_case = year % 400
b_case = year % 4
c_case = year % 400

if a_case and b_case == 0 and not c_case == 0:
    print(year, "SÍ es un año bisiesto.")
else:
    print(year, "NO es un año bisiesto.")

# salida
