from os import system
system("cls")

# entrada
print("Para salir del programa, ingrese 0 en todas las entradas.")
nonelderly = int(input("Ingrese el número de habitantes que NO SEAN DE TERCERA EDAD en su hogar: "))
income = float(input("Ingrese el monto total de ingresos en el hogar (sin puntos): "))
print()
elderly = int(input("Ingrese el número de personas de tercera edad en su hogar: "))

# proceso
familysize = elderly + nonelderly
if familysize == 0:
    print("Hasta luego.")
else:
    percapita_rent = income / familysize

    if familysize <= 4:
        if elderly >= 2:
            print("Su nivel socioeconómico es C3")
        else:
            if percapita_rent <= 60000:
                print("Su nivel socioeconómico es C3")
            if percapita_rent > 60000 and percapita_rent <= 100000:
                print("Su nivel socioeconómico es C2")
            if percapita_rent > 100000 and percapita_rent <= 300000:
                print("Su nivel socioeconómico es C1")
            if percapita_rent > 300000:
                print("Su nivel socioeconómico es AB")

    if familysize >= 5:
        if elderly >= 2:
            print("Su nivel socioeconómico es C3")
        else:
            if percapita_rent <= 40000:
                print("Su nivel socioeconómico es C3")
            if percapita_rent > 40000 and percapita_rent <= 80000:
                print("Su nivel socioeconómico es C2")
            if percapita_rent > 80000 and percapita_rent <= 250000:
                print("Su nivel socioeconómico es C1")
            if percapita_rent > 250000:
                print("Su nivel socioeconómico es AB")