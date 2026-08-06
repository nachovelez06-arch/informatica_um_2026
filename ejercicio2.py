def validar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")

    mayuscula = False
    minuscula = False
    numero = False
    especial = False

    especiales = "!@#$%&*?"

    for letra in password:
        if letra.isupper():
            mayuscula = True
        elif letra.islower():
            minuscula = True
        elif letra.isdigit():
            numero = True
        elif letra in especiales:
            especial = True

    if not mayuscula:
        errores.append("Debe tener una letra mayúscula")

    if not minuscula:
        errores.append("Debe tener una letra minúscula")

    if not numero:
        errores.append("Debe tener un número")

    if not especial:
        errores.append("Debe tener un carácter especial (!@#$%&*?)")

    return errores


def main():
    password = input("Ingrese una contraseña: ")

    errores = validar_password(password)

    if errores == []:
        print("La contraseña es segura.")
    else:
        print("La contraseña es insegura. Falta:")
        for error in errores:
            print("-", error)


main()