import sqlite3
conexion = sqlite3.connect('base.db')
mi_cursor = conexion.cursor()
mi_cursor.execute("insert into usuario values('2303','valentin','cliente','boquita123','laguzzivalen@gmail.com')")
conexion.commit()
conexion.close()



