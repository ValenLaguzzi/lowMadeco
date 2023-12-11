import sqlite3



def consultarEmail(mail):
    conexion = sqlite3.connect('base.db')
    mi_cursor = conexion.cursor()

    resultado = mi_cursor.execute("SELECT * FROM tabla_correos WHERE correo = ?", (mail,))
    

    conexion.close()

    return resultado is not None


def consultarContrasenia(password):
    conexion = sqlite3.connect('base.db')
    mi_cursor = conexion.cursor()

    resultado = mi_cursor.execute("SELECT * FROM tabla_contraseñas WHERE contraseña = ?", (password,))
    

    conexion.close()

    return resultado is not None


