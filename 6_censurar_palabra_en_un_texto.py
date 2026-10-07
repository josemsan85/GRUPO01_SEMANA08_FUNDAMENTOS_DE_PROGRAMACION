texto = "Este es un examen secreto con datos confidenciales"
palabras_prohibidas = ["secreto", "confidenciales"]

# Recorrer la lista y reemplazar cada palabra por '*' multiplicados por su longitud
for palabra in palabras_prohibidas:
    asteriscos = "*" * len(palabra)
    texto = texto.replace(palabra, asteriscos)

print(texto)