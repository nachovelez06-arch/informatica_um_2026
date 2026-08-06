biblioteca = [
    ["El Aleph", "Borges", 1949, False],
    ["Cien años de soledad", "Gabriel García Márquez", 1967, False],
    ["Rayuela", "Julio Cortázar", 1963, True],
    ["Ficciones", "Borges", 1944, False],
    ["Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True]
]


def mostrar_menu():
    print("\n--- BIBLIOTECA ---")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Libros disponibles")
    print("7. Libros prestados")
    print("8. Estadísticas")
    print("9. Salir")


def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    año = int(input("Año: "))

    biblioteca.append([titulo, autor, año, False])

    print("Libro agregado.")


def mostrar_libros(lista):
    if len(lista) == 0:
        print("No hay libros.")

    for libro in lista:
        estado = "Prestado" if libro[3] else "Disponible"

        print(
            libro[0],
            "-",
            libro[1],
            "-",
            libro[2],
            "-",
            estado
        )


def buscar_libro():
    texto = input("Buscar título: ").lower()

    encontrados = []

    for libro in biblioteca:
        if texto in libro[0].lower():
            encontrados.append(libro)

    if len(encontrados) == 0:
        print("No se encontraron libros.")
    else:
        mostrar_libros(encontrados)


def prestar_libro():
    titulo = input("Título del libro: ").lower()

    for libro in biblioteca:
        if libro[0].lower() == titulo:

            if libro[3]:
                print("El libro ya está prestado.")
            else:
                libro[3] = True
                print("Libro prestado.")

            return

    print("El libro no existe.")


def devolver_libro():
    titulo = input("Título del libro: ").lower()

    for libro in biblioteca:
        if libro[0].lower() == titulo:

            if libro[3]:
                libro[3] = False
                print("Libro devuelto.")
            else:
                print("El libro ya estaba disponible.")

            return

    print("El libro no existe.")


def mostrar_estado(prestado):
    hay_libros = False

    for libro in biblioteca:
        if libro[3] == prestado:
            print("-", libro[0])
            hay_libros = True

    if not hay_libros:
        print("No hay libros.")


def estadisticas():
    total = len(biblioteca)
    prestados = 0

    for libro in biblioteca:
        if libro[3]:
            prestados += 1

    print("\n--- ESTADÍSTICAS ---")
    print("Total:", total)
    print("Disponibles:", total - prestados)
    print("Prestados:", prestados)


def main():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            mostrar_libros(biblioteca)

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            prestar_libro()

        elif opcion == "5":
            devolver_libro()

        elif opcion == "6":
            print("\nLibros disponibles:")
            mostrar_estado(False)

        elif opcion == "7":
            print("\nLibros prestados:")
            mostrar_estado(True)

        elif opcion == "8":
            estadisticas()

        elif opcion == "9":
            print("Fin del programa.")
            break

        else:
            print("Opción incorrecta.")


main()