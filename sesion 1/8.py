while True:
    contraseña1 = input("Ingrese la contraseña: ")
    contraseña2 = input("Repita la contraseña: ")
    if contraseña1 == contraseña2:
        print("Contraseña confirmada.")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
