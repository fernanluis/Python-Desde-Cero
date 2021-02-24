import sqlite3 # módulo incluido en Python por defecto
from sqlite3 import Error

# para crear la primera conección a la base de datos que desea conectarse
# conexion = sqlite3.connect('database.db') # ejecutando el archivo creará el archivo database en el directorio de trabajo.
# crear un método conectar y colocar la primera conección
def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        print('Se ha conectado a la base de datos correctamente')
        return conexion # retornar la conección
    except Error:
        print('Ha ocurrido un error')

# crear tabla para la cuales necesaria una conección establecida utilizando un parámetro llamado conección.
def crear_tabla(conexion):
    # crear un cursor, que ejecuta ciertas sentencias de SQL como ser crear table, insertar datos, etc.
    cursor = conexion.cursor() # creando un cursor
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL)''' # sentencia SQL que se desea que ejecute ese cursor con los los campos que desea que tenga la tabla.

    cursor.execute(sentencia_sql)
    conexion.commit() #reflejar los cambios realizados
    conexion.close()# buena práctica cerrar la conección una vez finalizada la utilización

# insertar datos en la table, método con dos parámetros, primero la conección preestablecida y luego los datos que serán insertados en la tabla de ususario
def insertar(conexion, datos):
    # crear el cursor
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario(nombre, apellido) VALUES (?,?)' # nombre y apellidoson as columnas afectadas y (?,?) que indican los valores que serán recibidos como parámetros
    cursor.execute(sentencia_sql, datos) # ejecutar la sentencia pasandolé los datos que serán insertados.
    # actualización de la conección
    conexion.commit()
    # cerrar la conexion
    conexion.close()

# insertar varios registros utilizando 'many'
def insertar_varios(conexion, datos):
    # crear el cursor
    cursor = conexion.cursor()
    sentencia_sql = 'INSERT INTO usuario(nombre, apellido) VALUES (?,?)' # nombre y apellidoson as columnas afectadas y (?,?) que indican los valores que serán recibidos como parámetros
    cursor.executemany(sentencia_sql, datos) # ejecutar la sentencia pasandolé los datos que serán insertados.
    # actualización de la conección
    conexion.commit()
    # cerrar la conexion
    conexion.close()

# consultar datos pasando la conección como parámetro
def consultar(conexion):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario' # nombre, apellido o el asterisco para seleccionar todas las columnas
    cursor.execute(sentencia_sql) # devolverá los datos o los registros entonces se guadaran en un registro
    datos = cursor.fetchall() # aquí tendría todos los registro que se acaban de consultar y los almacenan en la variable datos.
    # no se realiza un commit porque no se estan insertando datos
    # cerrar la conección
    conexion.close()
    # retornar los datos
    return datos

# consultar un registro en específico mediante un id
def consultar_por_id(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario WHERE id=?' # nombre, apellido o el asterisco para seleccionar todas las columnas por id
    cursor.execute(sentencia_sql, (id,)) # al final una coma
    datos = cursor.fetchall() # aquí tendría todos los registro que se acaban de consultar y los almacenan en la variable datos.
    # no se realiza un commit porque no se estan insertando datos
    # cerrar la conección
    conexion.close()
    # retornar los datos
    return datos

# modificar y eliminar datos
def actualizar(conexion, id, nombre, apellido): # agregando campos a modificar
    cursor = conexion.cursor()
    sentencia_sql = 'UPDATE usuario SET nombre = ?, apellido = ? WHERE id = ?'
    cursor.execute(sentencia_sql, (nombre, apellido, id)) # usando tupla
    # actualización de la conección porque se ha modificado datos de la tbala ususario
    # actualización de la conección
    conexion.commit()
    # cerrar la conexion
    conexion.close()

# eliminar, pasando como parámetro la conección, el id
def eliminar(conexion, id):
    cursor = conexion.cursor()
    sentencia_sql = 'DELETE FROM usuario WHERE id = ?'
    cursor.execute(sentencia_sql, (id,))
    # actualización de la conección porque se ha modificado datos de la tabla usuaario
    # actualización de la conección
    conexion.commit()
    # cerrar la conexion
    conexion.close()


conexion = conectar()
# crear_tabla(conexion) comentado porque ya se creó la tabla
# datos = [('Luis', 'Ramos'), ('Ana', 'Ramos'), ('Didi', 'Lunguni')]
# insertar(conexion, datos) # parámetros conección y datos.
# insertar_varios(conexion, datos) ya se han insertado datos.

#datos = consultar(conexion) # datos retornados almacenarlo en una variable datos.
# mostrar datos
#for dato in datos:
#    print(dato[1] + ' ' + dato[2])

# En caso de producirse un error es posible manejarlo con un try y para ello, SQLite también incluye una función
# que se llama error que va a permitir manejar esta clase de errores.

# datos = consultar_por_id(conexion, 5)
# if len(datos) > 0: # comprobación para saber si el tamaño de los datos es mayor a cero, es decir, si encuentra el registro y si es así mostrar un print que imprima los datos en posición cero y asu vez en la posición 1.
#    print(datos[0][1] + ' ' + datos[0][2])
#else:
#    print('No se encontró ese usuario')

#actualizar(conexion, 2, 'Julia', 'Lunguni')
eliminar(conexion, 4)
