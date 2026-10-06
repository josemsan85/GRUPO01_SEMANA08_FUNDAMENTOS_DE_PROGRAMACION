tweet = "Aprendiendo #Python y #programacion con #DATOS en la UPN"
palabras = tweet.split()
hashtags = []
for palabra in palabras:
    if palabra.startswith("#"):
        hashtags.append(palabra.lower())
hashtags.sort()
print(hashtags)