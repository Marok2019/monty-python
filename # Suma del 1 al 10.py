# Determinar si un número es primo o no

# Entrada
n = 10

# Procesamiento
# Contador
divisores = 2

# Iterador
i = 2

# Búsqueda de divisores
while i <= n // 2:
    if n % i == 0:
        divisores += 1

    i += 1

# Salida
print(divisores)