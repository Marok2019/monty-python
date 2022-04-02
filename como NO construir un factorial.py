# ¿Cómo construir un factorial? (excepto que esto no sirve jajalol)

# entrada
a = int(input("Introduzca un factorial"))

# proceso
fact = 1

# iterador
i = a - 1

while i != 1:
	a *= i
	i -= 1
# salida
print("El factorial de", a, "es:", fact)