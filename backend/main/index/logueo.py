import re

def validar_correo_electronico(mail):

    mailStr = str (mail)

     # verifica que el correo tenga el formato correcto
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mailStr):
        return False
    else: 
        return True

import re

def validar_contrasenia(password):

    passwordStr = str (password)
 
    if len(passwordStr) < 8:
        return False
    
    if not any(char.islower() for char in passwordStr):
        return False
        
    if not any(char.isupper() for char in passwordStr):
        return False
        
    return True




