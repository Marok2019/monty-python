# entrada
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

# procesamiento (producto)
result = 0
sums_done = 1

while sums_done <= num2:
    result += num1
    sums_done += 1
    
# salida
print("Su resultado es:", result)