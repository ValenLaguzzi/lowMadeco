import re

def validar_correo_electronico(mail):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Utiliza re.match para verificar si el correo coincide con el patrón
    return re.match(patron, mail) is not None

import re

def validar_contrasenia(password):
    # Expresión regular para validar contraseñas
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Verificar si la contraseña cumple con el patrón
    if re.match(patron, password):
        return True
    else:
        return False




