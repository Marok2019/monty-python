from os import system
system("cls")

# entrada
number = int(input("Introduzca un número: "))

# proceso

# contadores
even_numbers = 0
odd_numbers = 0
greatest_input = 0
odd_sum = 0
avg_odd = 0

# ciclo
while number > 0:
    
    # inspector de pares    
    even_check = number % 2

    # cajón par
    if even_check == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

    # cajón impar 
        odd_sum += number
        avg_odd = odd_sum / odd_numbers

    # número mayor
    if number > greatest_input:
        greatest_input = number

    # repetidor de ciclo
    number = int(input("Introduzca un número: "))

# salida
print("El número de datos pares es: ", even_numbers)
print("-------------------------------------------")
print("El promedio de datos impares es: ", round(avg_odd))
print("-------------------------------------------")
print("El dato mayor es: ", greatest_input)