def obtener_dominio(email):
    # Limpiar espacios extremos y pasar a minúsculas
    email_limpio = email.strip().lower()
    
    # Verificar que contiene '@' y '.' con el operador 'in'
    if "@" in email_limpio and "." in email_limpio:
        # Separar por '@' y tomar la segunda parte (índice 1)
        partes = email_limpio.split("@")
        dominio = partes[1]
        return dominio
    else:
        return "El correo no es válido"

# Prueba
correo_prueba = "  Usuario@Dominio.Com  "
print("Dominio:", obtener_dominio(correo_prueba))