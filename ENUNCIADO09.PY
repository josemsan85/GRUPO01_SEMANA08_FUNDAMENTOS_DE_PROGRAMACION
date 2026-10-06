def analizar_frecuencia(parrafo, stopwords):
    texto = parrafo.lower()
    for signo in [".", ",", ";", ":", "!", "?"]:
        texto = texto.replace(signo, "")
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra not in stopwords:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias
parrafo = "Python es genial. Python es un lenguaje muy popular y genial."
vacias = ["es", "un", "de", "muy", "y"]

print(analizar_frecuencia(parrafo, vacias))