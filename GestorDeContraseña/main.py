import os
from getpass import getpass # pedir una contraseña por consola y que no se muestre

# generar una tabla para visualizar mejor los registros de la base de datos
from tabulate import tabulate # debe ser descargado 'pip install tabulate' porque noexiste en Python
from Conexion import * # importar el módulo de conexión de la base de datos.
# from Usuario import * da error
import Usuario
import Contrasena

conexion = conectar()
crear_tablas(conexion)

def inicio():
    os.system('cls')# acceder al sistema ejecutando la instrucción 'cls' para borrar todo lo que está en la consola cada vez que inicie la aplicación
    comprobar = Usuario.comprobar_usuario() #importando la clase Usuario
    if len(comprobar) == 0:
        print('Bienvenido, registre su información')
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        contrasena_maestra = getpass('Ingrese su contraseña maestra: ') # sin utilizar input para no mostrar la contraseña por consola
        respuesta = Usuario.registrar(nombre, apellido, contrasena_maestra)
        if respuesta == 'Registro correcto':
            print(f'Bienvenido {nombre}')
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
        respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra) # parámetro is y contrasena_maestra
        if len(respuesta) == 0:
            print('Contraseña incorrecta')
        else:
            print('Bienvenido')
            menu()

def menu():
    while True:
        print('Seleccione una de las siguientes opciones: ')
        print('\t-1 Añadir contraseña')
        print('\t-2 Ver todas las contraseñas')
        print('\t-3 Visualizar una contraseña')
        print('\t-4 Modificar contraseña')
        print('\t-5 Eliminar contraseña')
        print('\t-6 Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nueva_contrasena()
        elif opcion == '2':
            mostrar_contrasenas()
        elif opcion == '3':
            buscar_contrasena()
        elif opcion == '4':
            modificar_contrasena()
        elif opcion == '5':
            eliminar_contrasena()
        elif opcion == '6':
            break
        else:
            print('No ha ingresado una opción válida.')

# capturar los datos para registrar y también para mostrar lo que devuelve la función registrar contraseña
def nueva_contrasena():
    nombre = input('Ingrese el nombre: ')
    url = input('Ingrese la url: ')
    nombre_usuario = input('Ingrese el nombre de usuario: ')
    contrasena = input('Ingrese la contrasena: ')
    description = input('Ingrese la description: ')
    respuesta = Contrasena.registrar(nombre, url, nombre_usuario, contrasena, description)
    print(respuesta)

def mostrar_contrasenas():
    datos = Contrasena.mostrar()
    nuevos_datos = [] # nueva lista vacía
    headers = ['ID', 'NOMBRE', 'URL', 'USUARIO', 'CONTRASEÑA', 'DESCRIPTION']
    for dato in datos:# recorrer cada datos de sus datos, recorriendo cada una de las tuplas
        convertido = list(dato)
        convertido[4] = '********'
        nuevos_datos.append(convertido)
    # tabla = tabulate(datos, headers, tablefmt='fancy_grid') #tabla a mostrar
    tabla = tabulate(nuevos_datos, headers, tablefmt='fancy_grid') #tabla a mostrar
    # tablefmt le da un tipo de formato a la tabla
    print('\t\t\tTodas las contraseñas')
    print(tabla)

def buscar_contrasena():
    contrasena_maestra = getpass('Ingrese su contraseña maestra: ')#por seguridad ingresar su contraseña maestra
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print('Contraseña correcta')
    else:
        id = input('Ingrese el id de la contraseña a buscar: ')
        datos = Contrasena.buscar(id)
        headers = ['ID', 'NOMBRE', 'URL', 'USUARIO', 'CONTRASEÑA', 'DESCRIPTION']
        tabla = tabulate(datos, headers, tablefmt='fancy_grid') #tabla a mostrar
        # tablefmt le da un tipo de formato a la tabla
        print('\t\t\tTodas las contraseñas')
        print(tabla)

def modificar_contrasena():
    contrasena_maestra = getpass('Ingrese su contraseña maestra: ')#por seguridad ingresar su contraseña maestra
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print('Contraseña correcta')
    else:
        id = input('Ingrese el id de la contraseña a modificar: ')
        nombre = input('Ingrese el nuevo nombre: ')
        url = input('Ingrese la nueva url: ')
        nombre_usuario = input('Ingrese el nuevo nombre de usuario: ')
        contrasena = input('Ingrese la nueva contraseña: ')
        description = input('Ingrese la nueva descripción: ')
        respuesta = Contrasena.modificar(id, nombre, url, nombre_usuario, contrasena, description)
        print(respuesta)

def eliminar_contrasena():
    contrasena_maestra = getpass('Ingrese su contraseña maestra: ')#por seguridad ingresar su contraseña maestra
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print('Contraseña correcta')
    else:
        id = input('Ingrese el id de la contraseña a eliminar: ')
        respuesta = Contrasena.eliminar(id)
        print(respuesta)

inicio()
