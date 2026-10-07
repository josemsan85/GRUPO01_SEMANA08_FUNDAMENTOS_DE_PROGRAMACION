log_linea = '192.168.1.1 - - [10/Oct/2026:14:32:10 +0000] "GET /inicio/index.html HTTP/1.1" 200 4523'

# 1. Extraer la IP (primer elemento delimitado por espacios)
ip = log_linea.split(" ")[0]

# 2. Extraer el texto dentro de las comillas dobles usando find() y slicing
inicio_comillas = log_linea.find('"')
fin_comillas = log_linea.rfind('"')
peticion = log_linea[inicio_comillas + 1 : fin_comillas]  # "GET /inicio/index.html HTTP/1.1"

# Dividir la petición en Método, Ruta y Protocolo
partes_peticion = peticion.split(" ")
metodo = partes_peticion[0]
ruta = partes_peticion[1]

# 3. Extraer el código de estado (primer elemento después de la última comilla)
resto = log_linea[fin_comillas + 1 :].strip()
codigo_estado = resto.split(" ")[0]

# Reporte formateado
print(f"IP: {ip}")
print(f"Método HTTP: {metodo}")
print(f"Ruta: {ruta}")
print(f"Código de estado: {codigo_estado}")