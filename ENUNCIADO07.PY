lineas_csv = [
    "Ana, 18, Lima",
    "Carlos, 15, Arequipa",
    "María, 20, Trujillo"
]
print(f"{'Nombre':<10} | {'Nota':<5} | {'Ciudad':<10}")
print("-" * 30)
for linea in lineas_csv:
    partes = linea.split(",")
    nombre = partes[0].strip()
    nota = partes[1].strip()
    ciudad = partes[2].strip()
    print(f"{nombre:<10} | {nota:<5} | {ciudad:<10}")