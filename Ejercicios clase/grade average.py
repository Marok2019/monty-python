from os import system
system("cls")

# entrada
grade_student1 = float(input("Ingrese la primera nota: "))
grade2_student1 = float(input("Ingrese la segunda nota: "))

grade_student2 = float(input("Ingrese la primera nota: "))
grade2_student2 = float(input("Ingrese la segunda nota: "))

grade_student3 = float(input("Ingrese la primera nota: "))
grade2_student3 = float(input("Ingrese la segunda nota: "))

# proceso
avg1 = (grade_student1 + grade2_student1) / 2
avg2 = (grade_student2 + grade2_student2) / 2
avg3 = (grade_student3 + grade2_student3) / 2
avg_course = (avg1 + avg2 + avg3) / 3
round(avg_course, 1)
# salida
print("El promedio del estudiante 1 es: ", round(avg1, 1))
print("El promedio del estudiante 2 es: ", round(avg2, 1))
print("El promedio del estudiante 3 es: ", round(avg3, 1))
print("---------------------------------------")
print("El promedio del curso es: ", round(avg_course, 1))