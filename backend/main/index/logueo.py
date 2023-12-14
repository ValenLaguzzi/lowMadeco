import re

def validar_correo_electronico(mail):

    mailStr = str (mail)

     # verifica que el correo tenga el formato correcto
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mailStr):
        return True
    else: 
        return False

import re

def validar_contrasenia(password):

    passwordStr = str (password)
    # Longitud mínima de la contraseña
    if len(passwordStr) < 8:
        return False
    
    # letra minúscula
    if not any(char.islower() for char in passwordStr):
        return False
        
    # letra mayúscula
    if not any(char.isupper() for char in passwordStr):
        return False
        
    # Si todas las condiciones se cumplen, la contraseña es válida
    return True




