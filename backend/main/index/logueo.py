import re

def validar_correo_electronico(mail):
     # verifica que el correo tenga el formato correcto
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mail):
        return False
    else: 
        return True

import re

def validar_contrasenia(password):
    # Expresión regular para validar contraseñas
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Verificar si la contraseña cumple con el patrón
    if re.match(patron, password):
        return True
    else:
        return False




