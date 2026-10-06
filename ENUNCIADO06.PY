def censurar_texto(texto, prohibidas):
    texto_censurado = texto
    for palabra in prohibidas:
        asteriscos = "*" * len(palabra)
        texto_censurado = texto_censurado.replace(palabra, asteriscos)
    return texto_censurado
mensaje = "Este es un texto con contenido secreto e inapropiado"
lista_prohibida = ["secreto", "inapropiado"]

print(censurar_texto(mensaje, lista_prohibida))