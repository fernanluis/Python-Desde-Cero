import sqlite3 # módulo incluido en Python por defecto
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        print('Conexión a la base de datos correcta')
        return conexion # retornar la conección
    except Error:
        print('Ha ocurrido un error')

def crear_tablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql1 = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        contrasena_maestra TEXT NOT NULL
    )'''
    sentencia_sql2 = '''CREATE TABLE IF NOT EXISTS contrasena(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        url TEXT NOT NULL,
        nombre_usuario TEXT NOT NULL,
        contrasena TEXT NOT NULL,
        description TEXT
    )'''

    cursor.execute(sentencia_sql1)
    cursor.execute(sentencia_sql2)
    conexion.commit()
