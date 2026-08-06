def main():
    texto = input("Ingrese un texto: ")

    palabras = texto.split()

    cantidad_palabras = len(palabras)

    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

    cantidad_vocales = 0

    for letra in texto:
        if letra in vocales:
            cantidad_vocales += 1


    if cantidad_palabras > 0:
        palabra_larga = palabras[0]
        palabra_corta = palabras[0]

        for palabra in palabras:
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra

            if len(palabra) < len(palabra_corta):
                palabra_corta = palabra

    else:
        palabra_larga = ""
        palabra_corta = ""


    texto_modificado = ""

    for letra in texto:
        if letra in vocales:
            texto_modificado += "*"
        else:
            texto_modificado += letra


    inverso = palabras[::-1]

    print("Cantidad de palabras:", cantidad_palabras)
    print("Cantidad de vocales:", cantidad_vocales)
    print("Palabra más larga:", palabra_larga)
    print("Palabra más corta:", palabra_corta)
    print("Texto sin vocales:", texto_modificado)
    print("Palabras al revés:", " ".join(inverso))


main()