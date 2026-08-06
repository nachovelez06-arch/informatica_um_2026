def tabla_multiplicar(numero):
    print("Tabla del", numero)

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)


def tabla_completa(numero):
    print("Tabla completa")

    for fila in range(1, numero + 1):
        for columna in range(1, numero + 1):
            print(fila * columna, end=" ")

        print()


def triangulo(altura):
    print("Triángulo")

    for i in range(1, altura + 1):
        print("*" * i)


def triangulo_invertido(altura):
    print("Triángulo invertido")

    for i in range(altura, 0, -1):
        print("*" * i)


def main():
    tabla_multiplicar(5)

    print()

    tabla_completa(3)

    print()

    triangulo(4)

    print()

    triangulo_invertido(4)


main()