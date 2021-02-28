from Conexion import *

def registrar(nombre, url, nombre_usuario, contrasena, description):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = ''' INSERT INTO contrasema
        (nombre, url, nombre_usuario, contrasena, description)
        VALUE(?, ?, ?, ?, ?)'''
        datos = (nombre, url, nombre_usuario, contrasena, description)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Registro correcto'
    except Error as err:
        return 'Ha ocurridoun error ' + str(err)

#mostrar contraseñas de la tabla
def mostrar():
    datos = []
    try:
        conexion =conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contrasena'''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)
    # retornar los datos
    return datos

# buscar una contraseña con id de la contraseña que se quiere buscar
def buscar(id):
    datos = []
    try:
        conexion =conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contrasena WHERE id=? '''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)
    # retornar los datos
    return datos

# modificar contraseña en específico
def modificar(id, nombre, url, nombre_usuario, contrasena, description):
    try:
        conexion =conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contrasena SET nombre=?, url=?,
        nombre_usuario = ?, contrasena = ?, description = ? WHERE id = ?'''
        datos = (nombre, url, nombre_usuario, contrasena, description, id) # tupla
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Se modificó la contraseña'
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)

# eliminar
def eliminar(id):
    try:
        conexion =conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''DELETE FROM contrasena WHERE id = ?'''
        cursor.execute(sentencia_sql,(id,))
        conexion.commit()
        conexion.close()
        return 'Se eliminó la contraseña'
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)
