notas = []
aprobadas = []
desaprobadas = []
seguir = True
while seguir:
    nota = float(input("Ingrese una nota: "))
    notas.append(nota)
    if nota >= 12:
        aprobadas.append(nota)
    else:
        desaprobadas.append(nota)
    continuar = input("¿Desea seguir ingresando notas? (si/no): ")
    if continuar.lower() != "si":
        seguir = False
print("Notas aprobadas:", aprobadas)
print("Notas desaprobadas:", desaprobadas)