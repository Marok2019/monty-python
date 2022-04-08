from os import system
system("cls")

# Entradas
side_length = float(input("Tamaño del lado: "))
side_count = int(input("Número de lados: "))

# Proceso
perimeter = side_length*side_count

# Salida
print("El perímetro de un polígono de", side_count, "lados de tamaño",
      side_length, "cm", "es:", perimeter, "cm")
