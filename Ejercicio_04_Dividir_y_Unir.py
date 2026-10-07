# Ejercicio 4 - DIVIDIR Y UNIR PALABRAS
cadena = "rojo,verde,azul,amarillo"

# 1) Pasamos todo a mayúsculas
cadena = cadena.upper()

# 2) split() separa por la coma y devuelve una lista
colores = cadena.split(",")

# 3) join() une la lista usando ' | ' como separador
resultado = " | ".join(colores)

print(colores)
print(resultado)
