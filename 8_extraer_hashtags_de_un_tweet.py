tweet = "Hoy es un gran día para aprender #Python y #programacion con #miprofePercy"

# Separar el tweet en palabras
palabras = tweet.split()
hashtags = []

for palabra in palabras:
    # Verificar si inicia con '#'
    if palabra.startswith("#"):
        tag_limpio = palabra.lower()
        # Evitar duplicados
        if tag_limpio not in hashtags:
            hashtags.append(tag_limpio)

# Ordenar la lista alfabéticamente
hashtags.sort()

print("Hashtags extraídos:", hashtags)