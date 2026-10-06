cadena = "rojo, verde, azul, amarillo"
colores = cadena.split(", ")
colores_mayus = [color.upper() for color in colores]
resultado = " | ".join(colores_mayus)
print(resultado)