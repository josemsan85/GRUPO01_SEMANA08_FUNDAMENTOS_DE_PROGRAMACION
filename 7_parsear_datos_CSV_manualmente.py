datos_csv = """Ana,18,Lima
Carlos,15,Arequipa
Maria,20,Cusco"""

# Separar por líneas usando splitlines()
lineas = datos_csv.splitlines()

for linea in lineas:
    if linea:
        # Separar los datos por coma
        partes = linea.split(",")
        nombre = partes[0]
        nota = partes[1]
        ciudad = partes[2]
        
        # Mostrar el reporte formateado usando f-strings
        print(f"Estudiante: {nombre:<8} | Nota: {nota:<2} | Ciudad: {ciudad}")