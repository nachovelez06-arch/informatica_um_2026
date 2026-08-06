def pasar_a_celsius(valor, unidad):
    if unidad == "C":
        return valor
    elif unidad == "F":
        return (valor - 32) * 5 / 9
    elif unidad == "K":
        return valor - 273.15


def pasar_desde_celsius(valor, unidad):
    if unidad == "C":
        return valor
    elif unidad == "F":
        return valor * 9 / 5 + 32
    elif unidad == "K":
        return valor + 273.15


def main():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
    except:
        print("Error: Ingrese un número válido.")
        return

    origen = input("Unidad de origen (C/F/K): ").upper()
    destino = input("Unidad de destino (C/F/K): ").upper()

    if origen not in "CFK" or destino not in "CFK":
        print("Error: La unidad debe ser C, F o K.")
        return

    if origen == "K" and temperatura < 0:
        print("Error: La temperatura en Kelvin no puede ser menor a 0.")
        return

    celsius = pasar_a_celsius(temperatura, origen)
    resultado = pasar_desde_celsius(celsius, destino)

    print(f"{temperatura}°{origen} son {resultado:.2f}°{destino}")


main()