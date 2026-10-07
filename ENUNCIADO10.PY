log_linea = '192.168.1.1 - - [05/Oct/2026:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
ip = log_linea.split(" ")[0]
pos_inicio_comilla = log_linea.find('"') + 1
pos_fin_comilla = log_linea.find('"', pos_inicio_comilla)
peticion = log_linea[pos_inicio_comilla:pos_fin_comilla]
partes_peticion = peticion.split(" ")
metodo = partes_peticion[0]
ruta = partes_peticion[1]
resto_log = log_linea[pos_fin_comilla + 2:]
codigo_estado = resto_log.split(" ")[0]
print(f"IP: {ip}")
print(f"Método HTTP: {metodo}")
print(f"Ruta: {ruta}")
print(f"Código de Estado: {codigo_estado}")
#