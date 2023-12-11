import re

def validar_correo_electronico(mail):
     # verifica que el correo tenga el formato correcto
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mail):
        return False
    else: 
        return True

import re

def validar_contrasenia(password):
    # Longitud mínima de la contraseña
    if len(password) < 8:
        return False
    
    # Al menos una letra minúscula
    if not re.search(c ['a-z'] for c in password):
        return False
    
    # Al menos una letra mayúscula
    if not any(c ['A-Z'] for c in password):
        return False
    
    # Al menos un dígito
    if not any(c in ['0-9'] for c in password):
        return False
    
    # Al menos un carácter especial
    if not any(c in ['@', '$', '!', '%', '*', '?', '&'] for c in password):
        return False
    
    # Si todas las condiciones se cumplen, la contraseña es válida
    return True




