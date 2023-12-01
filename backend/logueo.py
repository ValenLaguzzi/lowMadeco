import re

def validar_correo_electronico(mail):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Utiliza re.match para verificar si el correo coincide con el patrón
    return re.match(patron, mail) is not None
