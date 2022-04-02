# Entradas
PI = 3.14
sph_ratio = float(input("Radio de la esfera: "))
sph_area = 4 * PI * sph_ratio ** 2
sph_vol = (4/3) * PI * sph_ratio ** 3

# Proceso (cálculo área y volumen esfera)
area = sph_area
volume = sph_vol

# Salida
print("El área de una esfera de radio", sph_ratio, "es:", sph_area, "cm^2")
print("El volumen de una esfera de radio", sph_ratio, "es:", sph_vol, "cm^3")      
