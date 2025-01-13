asignaturas = []
notas = []

print("Ingrese los nombres de 5 asignaturas y sus respectivas notas:")

for i in range(1, 6):

    asignatura = input(f"Ingrese el nombre de la asignatura {i}: ")
    asignaturas.append(asignatura)

    while True:
        try:
            nota = float(input(f"Ingrese la nota de {asignatura}: "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("Por favor, ingrese una nota válida entre 0 y 20.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

print("\nResumen de notas:")
for asignatura, nota in zip(asignaturas, notas):
    print(f"En la asignatura {asignatura} sacó {nota}.")