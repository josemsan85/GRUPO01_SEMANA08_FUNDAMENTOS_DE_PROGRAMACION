# Ejercicio 6 - CENSURAR PALABRA EN UN TEXTO
texto = "eres un tonto y un feo"
prohibidas = ["tonto", "feo"]

for palabra in prohibidas:
    # "*" * len(palabra) crea asteriscos del mismo largo
    asteriscos = "*" * len(palabra)
    texto = texto.replace(palabra, asteriscos)

print(texto)
