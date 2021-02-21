# Python también admite el paradigma de programación funcional, en el que las
# funciones se tratan como valores como cualquier otra variable.

# En Programación Funcional las funciones son tratadas como ciudadanos de primera
# (first-class citizens), lo que significa que se le pueden asociar nombres,
# pueden ser pasadas como argumentos o retornadas desde otras funciones,
# como cualquier otro tipo de datos.

# Lo que permite que los programas sean escritos en estilos declarativos y compuestos,
# donde las pequeñas funciones son combinadas en manera modular.
# Surgió del ámbito científico universitario gracias al calculo lambda,
# que era un sistema formal de computo basado en solamente funciones.

# Decorators

# Una cosa que la programación funcional hace posible es la idea de un decorador,
# que es una función de orden superior que puede modificar otra función.

# Por ejemplo, escriba un decorador que anuncie cuándo una función está
# a punto de comenzar y cuándo termina.
# Luego podemos aplicar este decorador usando un símbolo @.
def mi_mensaje(f):
    def wrapper():
        print("A punto de correr la función")
        f()
        print("Finalizada la función")
    return wrapper # si no usamos return TypeError: 'NoneType' object is not callable
@mi_mensaje
def hola():
    print("¡Hola, mundo!")

hola() # sin llamarla no imprime nada

""" Salida:
A punto de correr la función
¡Hola, mundo!
Finalizada la función
"""

# Funciones lambda
# Las funciones Lambda proporcionan otra forma de crear funciones en Python. Por ejemplo,
# si queremos definir la misma función cuadrado que hicimos en la clase anterior,
# podemos escribir:
cuadrado = lambda x: x * x
# Donde la entrada está a la izquierda de : y la salida está a la derecha.

# Esto puede ser útil cuando no queremos escribir una función completamente
# separada para un solo uso pequeño. Por ejemplo, si queremos ordenar algunos
# objetos en los que al principio no está claro cómo ordenarlos.
# Imagina que tenemos una lista de personas, pero con nombres y casas en lugar
# de solo nombres que deseamos ordenar:
personas = [
{"nombre": "Harry", "casa": "Gryffindor"},
{"nombre": "Cho", "casa": "Ravenclaw"},
{"nombre": "Draco", "casa": "Slytherin"} ]
# ¡CUIDADO!
personas.sort()
print(personas)

# El codigo de nuestro diccionario produce un error:

# Traceback (most recent call last):
#  File "j_programacionFuncional9.py", line 57, in <module>
#    personas.sort()
# TypeError: '<' not supported between instances of 'dict' and 'dict'

# Esto ocurre porque Python no sabe cómo comparar dos diccionarios para comprobar
# si uno es menor que el otro. Podemos resolver este problema incluyendo un argumento
# key para la función sort, que especifica qué parte del diccionario deseamos usar para ordenar.

# Veamos.
