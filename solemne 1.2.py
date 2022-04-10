from os import system
system("cls")

#entradas
t = int(input("Ingrese el instante de tiempo t: "))

#procesos

speed_0 = 10
speed_1 = 20

a = ((speed_1 - speed_0) / t)
pos = ((speed_0 * t) + (a * t ** 2) / 2)

# salida
print("La aceleración de la partícula es", a, "m/s^2", "y la posición es", pos)