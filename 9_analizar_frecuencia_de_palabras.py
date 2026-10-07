def analizar_frecuencia(texto):
    # Lista de palabras vacías (stopwords) a ignorar
    stopwords = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "por", "un", "para", "con", "no", "una", "su", "al", "es"]
    
    # Signos de puntuación a eliminar
    puntuaciones = [".", ",", ";", ":", "!", "?", "(", ")", '"']
    
    # Normalizar a minúsculas
    texto_limpio = texto.lower()
    
    # Eliminar puntuación usando replace()
    for signo in puntuaciones:
        texto_limpio = texto_limpio.replace(signo, "")
    
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        if palabra not in stopwords:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias

# Prueba
parrafo = "Python es un lenguaje de programación. Python es genial y Python es muy fácil."
print(analizar_frecuencia(parrafo))