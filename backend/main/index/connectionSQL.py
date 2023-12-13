import sqlite3



def consultarEmail(mail):
    conexion = sqlite3.connect('C:\Desarrollo\Mis Proyectos\lowMadeco\base.db')
    mi_cursor = conexion.cursor()

    resultado = mi_cursor.execute("SELECT * FROM usuarios WHERE correo = ?", (mail))
    

    conexion.close()

    return resultado is not None


def consultarContrasenia(password):
    conexion = sqlite3.connect('C:\Desarrollo\Mis Proyectos\lowMadeco\base.db')
    mi_cursor = conexion.cursor()

    resultado = mi_cursor.execute("SELECT * FROM usuarios WHERE contraseña = ?", (password))
    

    conexion.close()

    return resultado is not None


