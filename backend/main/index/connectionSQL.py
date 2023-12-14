import sqlite3



def consultarDominio(mail, password):
    try:
        conexion = sqlite3.connect('C:/Desarrollo/Mis Proyectos/lowMadeco/base.db')
        mi_cursor = conexion.cursor()

        mail_str = str(mail)

        mi_cursor.execute('SELECT contrasenia FROM usuario WHERE email = ?', (mail_str,))
        resultado = mi_cursor.fetchone()

        if password ==  resultado[0]:
         return True
        
    except sqlite3.Error as e:
        print(f"error: {e}")
    finally:
       
        conexion.close()

    



   

    