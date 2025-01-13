objetivo = float(input("Ingrese la cantidad que desea ahorrar: "))
ahorrado = 0

while ahorrado < objetivo:
    cantidad = float(input("Ingrese la cantidad a ahorrar: "))
    ahorrado += cantidad
    print(f"Total ahorrado: {ahorrado:.2f}")

print("¡Has alcanzado tu objetivo de ahorro!")
