# entrada
loops = int(input("Introduzca el número de ciclos para la palabra Hola!: "))

# proceso
# contador
loop_count = loops

while loop_count > 0:
	print("Hola!")
	loop_count -= 1
	
# salida
print("Se ha dicho Hola!", loops, "veces.")