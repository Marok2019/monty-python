from os import system
system("cls")

# entrada
print("Bienvenido a Mamá Juana")
pizza_quantity = int(input("Cuántas pizzas desea ordenar: "))
v_ingredientes = ['tomato', 'pineapple', 'pepperoni', 'olives']
v_ingPrecios = [300, 500, 400, 600]

# proceso
if pizza_quantity == 0:
    print("Hasta luego.")
else:
    i = pizza_quantity
    subtotal = 1000 * pizza_quantity
    ingredient_sum = 0

    while i > 0:
        tomato = 1 
        pineapple = 2
        pepperoni = 3
        olives = 4

        ingredient_quantity = int(input("Ingrese la cantidad de ingredientes de su pizza: "))

        if ingredient_quantity == 1:
            ingredient_sum += 1
            ingredient1 = int(input("Ingrese el ingrediente 1: "))

            while ingredient1 < 1 or ingredient1 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient1 = int(input("Ingrese el ingrediente 1: "))


            print("** ", v_ingredientes[ingredient1])

            if ingredient1 == tomato:
                subtotal += 300
            if ingredient1 == pineapple:
                subtotal += 500
            if ingredient1 == pepperoni:
                subtotal += 400
            if ingredient1 == olives:
                subtotal += 600

        if ingredient_quantity == 2:
            ingredient_sum += 2
            ingredient1 = int(input("Ingrese el ingrediente 1: "))

            while ingredient1 < 1 or ingredient1 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient1 = int(input("Ingrese el ingrediente 1: "))

            if ingredient1 == tomato:
                subtotal += 300
            if ingredient1 == pineapple:
                subtotal += 500
            if ingredient1 == pepperoni:
                subtotal += 400
            if ingredient1 == olives:
                subtotal += 600

            ingredient2 = int(input("Ingrese el ingrediente 2: "))
            while ingredient2 < 1 or ingredient2 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient2 = int(input("Ingrese el ingrediente 2: "))

            if ingredient2 == tomato:
                subtotal += 300
            if ingredient2 == pineapple:
                    subtotal += 500
            if ingredient2 == pepperoni:
                 subtotal += 400
            if ingredient2 == olives:
                subtotal += 600

        if ingredient_quantity == 3:
            ingredient_sum += 3
            ingredient1 = int(input("Ingrese el ingrediente 1: "))

            while ingredient1 < 1 or ingredient1 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient1 = int(input("Ingrese el ingrediente 1: "))

            if ingredient1 == tomato:
                subtotal += 300
            if ingredient1 == pineapple:
                subtotal += 500
            if ingredient1 == pepperoni:
                subtotal += 400
            if ingredient1 == olives:
                subtotal += 600

            ingredient2 = int(input("Ingrese el ingrediente 2: "))
            while ingredient2 < 1 or ingredient2 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient2 = int(input("Ingrese el ingrediente 2: "))

            if ingredient2 == tomato:
                subtotal += 300
            if ingredient2 == pineapple:
                    subtotal += 500
            if ingredient2 == pepperoni:
                 subtotal += 400
            if ingredient2 == olives:
                subtotal += 600

            ingredient3 = int(input("Ingrese el ingrediente 3: "))
            while ingredient3 < 1 or ingredient3 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient3 = int(input("Ingrese el ingrediente 3: "))

            if ingredient3 == tomato:
                subtotal += 300
            if ingredient3 == pineapple:
                subtotal += 500
            if ingredient3 == pepperoni:
                subtotal += 400
            if ingredient3 == olives:
                subtotal += 600


        if ingredient_quantity == 4:
            ingredient_sum += 4
            ingredient1 = int(input("Ingrese el ingrediente 1: "))

            while ingredient1 < 1 or ingredient1 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient1 = int(input("Ingrese el ingrediente 1: "))

            if ingredient1 == tomato:
                subtotal += 300
            if ingredient1 == pineapple:
                subtotal += 500
            if ingredient1 == pepperoni:
                subtotal += 400
            if ingredient1 == olives:
                subtotal += 600

            ingredient2 = int(input("Ingrese el ingrediente 2: "))
            while ingredient2 < 1 or ingredient2 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient2 = int(input("Ingrese el ingrediente 2: "))

            if ingredient2 == tomato:
                subtotal += 300
            if ingredient2 == pineapple:
                    subtotal += 500
            if ingredient2 == pepperoni:
                 subtotal += 400
            if ingredient2 == olives:
                subtotal += 600

            ingredient3 = int(input("Ingrese el ingrediente 3: "))
            while ingredient3 < 1 or ingredient3 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient3 = int(input("Ingrese el ingrediente 3: "))

            if ingredient3 == tomato:
                subtotal += 300
            if ingredient3 == pineapple:
                subtotal += 500
            if ingredient3 == pepperoni:
                subtotal += 400
            if ingredient3 == olives:
                subtotal += 600

            ingredient4 = int(input("Ingrese el ingrediente 4: "))
            while ingredient4 < 1 or ingredient4 > 4:
                print("Por favor, un ingrediente válido.")
                ingredient4 = int(input("Ingrese el ingrediente 4: "))

            if ingredient4 == tomato:
                subtotal += 300
            if ingredient4 == pineapple:
                subtotal += 500
            if ingredient4 == pepperoni:
                subtotal += 400
            if ingredient4 == olives:
                subtotal += 600

        if pizza_quantity % 2 == 0 and ingredient_sum % 2 == 0:
            print("Subtotal", "$", subtotal)
            print("Su compra tiene un 10% de descuento")
        else:
            print("Subtotal", "$", subtotal)
        i -= 1

    total = subtotal
    total_discounted = total - (total * 0.1)
    if pizza_quantity % 2 == 0 and ingredient_sum % 2 == 0:
        print("El total es", "$", total_discounted)
    else:
        print("El total es", "$", total)
