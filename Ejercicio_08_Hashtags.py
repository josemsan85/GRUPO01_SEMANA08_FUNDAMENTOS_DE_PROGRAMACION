# Ejercicio 8 - EXTRAER HASHTAGS DE UN TWEET
tweet = "Aprendiendo #Python en la #UPN, que buen #Curso!"

palabras = tweet.split()
hashtags = []

for palabra in palabras:
    if palabra.startswith("#"):
        # strip() también quita signos de los bordes (coma, signo de exclamación)
        limpio = palabra.strip(",.!?").lower()
        hashtags.append(limpio)

# Ordenamos la lista alfabéticamente
hashtags.sort()

print(hashtags)
