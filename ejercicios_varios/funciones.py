def mi_function():
    print('Mi primera función en Python')

mi_function() # llamando a la función para mostrar el mensaje

# para añadir parámetros a la función
def mi_function(param1, param2):
    print('Mi primera función en Python')

mi_function('Hola', 2) # llamando a la función para mostrar el mensaje

# para añadir parámetros a la función y mostrar los parámetros
def mi_function(param1, param2):
    print('El parámetro 1 es: ' + str(param1) + ' y ' + 'El parámetro 2 es: '  + str(param2))

mi_function('Hola', 2) # llamando a la función para mostrar el mensaje
# la función espera 2 parámetros, por lo tanto, en caso de envairle solo uno dará error.

# especificar el orden de los parámetros
def mi_function(param1, param2):
    print('El parámetro 1 es: ' + str(param1) + ' y ' + 'El parámetro 2 es: ' + str(param2))

mi_function(param2='Hola', param1=2) # llamando a la función para mostrar el mensaje

# parámetros por defecto
def mi_function(texto1, texto2 = 'y Este es el texto 2' ):
    print(texto1, texto2, sep = '\n')

mi_function('Este es el texto 1', 'y Este es el texto 2 modificado') # llamando a la función para mostrar el mensaje

# pasar más parámetros de los ya establecidos. se crea un parámetro de tipo tupla
def mi_function(texto1, texto2, *otros_parametros):
    print(otros_parametros)

mi_function('Este es el texto 1', 'Este es el texto 2', 1, 2, True) # llamando a la función para mostrar el mensaje

# también es posible recibir datos de tipo diccionario
def mi_function(texto1, texto2, **otros_parametros):
    print(otros_parametros)

mi_function('Este es el texto 1', 'Este es el texto 2', valor1 = 1, valor2 = 2,  valor = True) # llamando a la función para mostrar el mensaje

# acceder a uno de los datos del diccionario
def mi_function(texto1, texto2, **otros_parametros):
    print(otros_parametros['valor1'])

mi_function('Este es el texto 1', 'Este es el texto 2', valor1 = 1, valor2 = 2,  valor = True) # llamando a la función para mostrar el mensaje

# retornar valores
def asignar_valor(x, y):
    x = x + 1
    y = y + 1
    return x, y # python añade ambos valores a una tupla

print(asignar_valor(3, 4))
