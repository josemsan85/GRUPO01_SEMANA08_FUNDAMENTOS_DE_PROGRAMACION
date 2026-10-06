def validar_y_obtener_dominio(email):
    email_clean = email.strip().lower()
    if "@" in email_clean and "." in email_clean:
        partes = email_clean.split("@")
        dominio = partes[1]
        return dominio
    else:
        return "Correo no válido"
print(validar_y_obtener_dominio("  Usuario@Dominio.com  "))
print(validar_y_obtener_dominio("  PanchoMencho.com"))