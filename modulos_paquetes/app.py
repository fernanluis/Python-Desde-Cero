# import mi_modulo # módulo propio
import paquete.mi_modulo # cambiando modulo a un paquete
# import os # acceder a las funcionalidades del sistema operativo
# import sys # acceder a las funcionalidades del intérprete de Python
import time # módulo que permitirá manipular fechas y horas.
# import os, sys, time separados por coma en una misma línea
#otra forma de importar es con la siguinete línea
from time import asctime
from paquete.mi_modulo import mensaje
from paquete.operaciones import suma
from paquete.operaciones import resta
from paquete.operaciones import multiplicar
from paquete.operaciones import dividir
# from paquete.operaciones import suma, resta, multiplicar, dividir en un sola línea
# from paquete.operaciones import * el asterisco llama a todas las funciones que contiene.

#print(mi_modulo)
#print(mi_modulo.mensaje())
print(paquete.mi_modulo)
print(paquete.mi_modulo.mensaje())
print(mensaje())
print(time.asctime()) # acceder a la hora actual
print(asctime()) # importando con 'from time import asctime'

print(suma(2, 2))
print(resta(2, 2))
print(multiplicar(2, 2))
print(dividir(2, 2))
