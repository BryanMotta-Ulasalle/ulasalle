class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Vehículo de color {self.color} con {self.ruedas} ruedas"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # en km/h
        self.cilindrada = cilindrada  # en cc

    def __str__(self):
        return (super().__str__() +
                f", velocidad máxima de {self.velocidad} km/h y cilindrada de {self.cilindrada} cc")


class Bicicleta(Vehiculo):
    TIPOS_VALIDOS = {"urbana", "deportiva"}

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido: {tipo}. Los tipos válidos son: {self.TIPOS_VALIDOS}")
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", tipo {self.tipo}"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga  # en kg

    def __str__(self):
        return super().__str__() + f" y capacidad de carga de {self.carga} kg"


class Motocicleta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)

    def __str__(self):
        return super().__str__()


if __name__ == "__main__":
    vehiculo = Vehiculo("rojo", 4)
    print(vehiculo)

    coche = Coche("azul", 4, 180, 2000)
    print(coche)

    bicicleta = Bicicleta("verde", 2, "urbana")
    print(bicicleta)

    camioneta = Camioneta("negra", 4, 150, 3000, 500)
    print(camioneta)

    motocicleta = Motocicleta("blanca", 2, 220, 600)
    print(motocicleta)
