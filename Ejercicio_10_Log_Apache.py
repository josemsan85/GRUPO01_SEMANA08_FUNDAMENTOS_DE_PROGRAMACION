# Ejercicio 10 - EXTRAER DATOS DE UN LOG DE SERVIDOR WEB (formato Apache)
logs = [
    '192.168.1.10 - - [10/Oct/2026:13:55:36 -0500] "GET /index.html HTTP/1.1" 200 2326',
    '10.0.0.5 - - [10/Oct/2026:13:56:01 -0500] "POST /login HTTP/1.1" 302 512',
    '172.16.0.8 - - [10/Oct/2026:13:57:10 -0500] "GET /imagen.png HTTP/1.1" 404 128',
]

for linea in logs:
    partes = linea.split()   # separa por espacios

    ip = partes[0]
    metodo = partes[5].replace('"', "")   # quita la comilla de "GET
    ruta = partes[6]
    codigo = partes[8]

    print(f"IP: {ip} | Método: {metodo} | Ruta: {ruta} | Código: {codigo}")
