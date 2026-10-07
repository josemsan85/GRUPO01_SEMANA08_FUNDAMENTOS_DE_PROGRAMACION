cadena = "rojo,verde,azul,amarillo"

# 1. Separar la cadena por comas
colores = cadena.split(",")

# 2. Convertir cada palabra a mayúsculas
colores_mayus = [color.upper() for color in colores]

# 3. Unir los elementos con ' | '
resultado = " | ".join(colores_mayus)

print(resultado)