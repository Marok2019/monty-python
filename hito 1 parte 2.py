from os import system
system("cls")

# entrada
n = int(input("Introduzca un número natural: "))
print("Su número natural es ", n)

# proceso
sum_n = n * (n + 1) // 2
print(sum_n)
