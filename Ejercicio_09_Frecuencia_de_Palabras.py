# Ejercicio 9 - ANALIZAR FRECUENCIA DE PALABRAS
def frecuencia_palabras(parrafo):
    # Palabras vacías (stopwords) que vamos a ignorar
    stopwords = ["el", "la", "los", "las", "de", "y", "en", "un", "una",
                 "es", "que", "a", "con", "por", "para", "del", "al"]

    # Pasamos a minúsculas
    parrafo = parrafo.lower()

    # Quitamos los signos de puntuación con replace()
    for signo in [".", ",", ";", ":", "!", "?", "¿", "¡"]:
        parrafo = parrafo.replace(signo, "")

    # Separamos en palabras
    palabras = parrafo.split()

    # Contamos con un diccionario
    frecuencia = {}
    for palabra in palabras:
        if palabra not in stopwords:
            if palabra in frecuencia:
                frecuencia[palabra] = frecuencia[palabra] + 1
            else:
                frecuencia[palabra] = 1

    return frecuencia


texto = "Python es genial. Python es un lenguaje fácil, y el lenguaje Python es popular!"
resultado = frecuencia_palabras(texto)
print(resultado)
