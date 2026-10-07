# Ejercicio 7 - PARSEAR DATOS CSV MANUALMENTE
lineas = [
    "Ana,18,Lima",
    "Luis,15,Cusco",
    "Maria,20,Arequipa",
]

print("REPORTE DE NOTAS")
print("-" * 30)
print(f"{'Nombre'.ljust(10)}{'Nota'.rjust(5)}  Ciudad")
print("-" * 30)

for linea in lineas:
    partes = linea.split(",")
    nombre = partes[0]
    nota = partes[1]
    ciudad = partes[2]
    print(f"{nombre.ljust(10)}{nota.rjust(5)}  {ciudad}")
