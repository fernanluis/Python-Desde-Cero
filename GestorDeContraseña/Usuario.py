# importar el módulo hashlib que va a permitir encriptar la contraseña de la aplicación
import hashlib
from Conexion import *

def comprobar_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario'
    cursor.execute(sentencia_sql)
    usuario_encontrado = cursor.fetchall() # aquí tendría todos los registro que se acaban de consultar y los almacenan en la variable usuario encontrado.
    conexion.close()
    return usuario_encontrado

# función para registrar
def registrar(nombre, apellido, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO usuario
        (nombre, apellido, contrasena_maestra)
        VALUES(?,?,?)'''# valores a insertar
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()# encriptar la contraseña con al contraseña que se recibe como parámetro convertido a una cadena exagesimal
        datos = (nombre, apellido,cm_cifrada)# tupla de datos que recibe el nombre como parámetro
        cursor.execute(sentencia_sql, datos) # con el cursor ejecutar la secuencia de sql de insert pasando además la tupla como parámetro
        conexion.commit()
        conexion.close()
        return 'Registro correcto'
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)

#print(comprobar_usuario())
#print(registrar('Luis', 'Ramos', '12345'))
#print(comprobar_usuario())

# una vez creada la contraseña, se va a comprobar la misma
# contraseá maestra debe coincidir con la contraseña pasada como parámetro
# luego cifrar nuevamente para comprobar con la contraseña cifrada que ya existe en la base de datos.

def comprobar_contrasena(id, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM usuario
        WHERE id = ? AND contrasena_maestra = ?'''
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()
        cursor.execute(sentencia_sql, (id, cm_cifrada))
        datos = cursor.fetchall() # almacenar lo que devuelve el cursor
        conexion.close()
        return datos
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)

# print(comprobar_contrasena(1, '12345'))
