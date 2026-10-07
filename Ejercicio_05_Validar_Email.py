# Ejercicio 5 - VALIDAR Y FORMATEAR CORREO ELECTRÓNICO
def validar_email(email):
    # Limpiamos: quitamos espacios y pasamos a minúsculas
    email = email.strip().lower()

    # Verificamos que tenga '@' y '.'
    if "@" in email and "." in email:
        partes = email.split("@")   # separa usuario y dominio
        dominio = partes[1]
        return dominio
    else:
        return "Email inválido"


correo = input("Escribe tu correo: ")
resultado = validar_email(correo)
print(f"Dominio: {resultado}")
