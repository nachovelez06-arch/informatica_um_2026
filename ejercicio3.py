def promedio(notas):
    return sum(notas) / len(notas)


def contar_aprobados(notas):
    cantidad = 0

    for nota in notas:
        if nota >= 6:
            cantidad += 1

    return cantidad


def distribucion(notas):
    bajos = 0
    medios = 0
    buenos = 0
    excelentes = 0

    for nota in notas:
        if nota <= 3:
            bajos += 1
        elif nota <= 5:
            medios += 1
        elif nota <= 7:
            buenos += 1
        else:
            excelentes += 1

    return bajos, medios, buenos, excelentes


def main():
    while True:
        try:
            cantidad = int(input("¿Cuántas notas va a ingresar? "))

            if cantidad > 0:
                break
            else:
                print("Debe ser un número mayor a 0.")

        except:
            print("Ingrese un número válido.")

    notas = []

    for i in range(cantidad):
        while True:
            try:
                nota = int(input(f"Ingrese la nota {i + 1}: "))

                if 1 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1 y 10.")

            except:
                print("Ingrese un número entero.")

    aprobados = contar_aprobados(notas)
    porcentaje = aprobados * 100 / cantidad

    bajos, medios, buenos, excelentes = distribucion(notas)

    print("\n--- RESULTADOS ---")
    print("Notas:", notas)
    print("Promedio:", round(promedio(notas), 2))
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))
    print(f"Aprobados: {aprobados} de {cantidad} ({porcentaje:.0f}%)")

    print("Distribución:")
    print("1 a 3:", bajos)
    print("4 a 5:", medios)
    print("6 a 7:", buenos)
    print("8 a 10:", excelentes)


main()