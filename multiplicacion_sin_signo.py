# entrada
a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))

# procesamiento (producto)
c = 0
# iterador
sums_done = 1

while sums_done <= b:
    c += a
    sums_done += 1
    
# salida
print("Su resultado es:", c)