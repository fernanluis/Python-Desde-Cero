# for i in range(10):
# print(f"El cuadrado de {i} es {cuadrado(i)}")

# Tener en cuenta el archivo funciones6.py

# Nos encontramos con este problema porque, de forma predeterminada, los archivos de Python
# no se conocen entre sí, por lo que tenemos que importar explícitamente la función cuadrado
# del módulo de funciones que acabamos de escribir en modulos7.py

from funciones6 import cuadrado

for i in range(10):
    print(f"El cuadrado de {i} es {cuadrado(i)}")

# Alternativamente, podemos optar por importar todo el módulo de funciones y luego usar
# la notación de puntos para acceder a la función cuadrada:

import funciones6
for i in range(10):
    print(f"El cuadrado de {i} es {funciones6.cuadrado(i)}")

# Hay muchos módulos de Python integrados que podemos importar, como
# math
# csv
