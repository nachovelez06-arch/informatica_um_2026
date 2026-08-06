def cargar_productos():
    productos = []

    print("Ingrese productos. Escriba 'fin' para terminar.")

    while True:
        nombre = input("Producto: ")

        if nombre.lower() == "fin":
            break

        try:
            precio = float(input("Precio: "))

            if precio < 0:
                print("El precio no puede ser negativo.")
                continue

            productos.append([nombre, precio])

        except:
            print("Ingrese un precio válido.")

    return productos


def calcular_subtotal(productos):
    total = 0

    for producto in productos:
        total += producto[1]

    return total


def calcular_descuento(subtotal, cantidad, club):
    descuento = 0

    if subtotal > 50000:
        descuento = subtotal * 0.15
    elif subtotal > 20000:
        descuento = subtotal * 0.10
    elif subtotal > 10000:
        descuento = subtotal * 0.05

    if cantidad > 5:
        descuento += 1000

    if club:
        descuento += (subtotal - descuento) * 0.05

    return descuento


def mostrar_compra(productos, subtotal, descuento, total):
    print("\n--- RESUMEN DE COMPRA ---")

    for producto in productos:
        print(producto[0], "- $", producto[1])

    print("Subtotal: $", round(subtotal, 2))
    print("Descuento: $", round(descuento, 2))
    print("Total final: $", round(total, 2))


def main():
    respuesta = input("¿Es socio del club? (s/n): ")

    club = respuesta.lower() == "s"

    productos = cargar_productos()

    if len(productos) == 0:
        print("No hay productos cargados.")
        return

    subtotal = calcular_subtotal(productos)

    descuento = calcular_descuento(
        subtotal,
        len(productos),
        club
    )

    total = subtotal - descuento

    mostrar_compra(productos, subtotal, descuento, total)


main()