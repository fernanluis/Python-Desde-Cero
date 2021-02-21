print('Esto es' + ' ' + 'un texto')

print('Mi nombre es {} {}'.format('Luis', 'Ramos')) # format requiere 2 parámetros

print('Mi nombre es {0} {1}. Buenvenidos al curso de {2}'.format('Luis', 'Ramos', 'Python')) # por posiciones, desde el número cero.

print('Mi nombre es {1} {0}. Buenvenidos al curso de {2}'.format('Luis', 'Ramos', 'Python')) # inviertiendo los valores

print('Mi nombre es {1} {0}. Buenvenidos al curso de {2}'.format(input('Ingrese su nombre: '), input('Ingrese su apellido: '), 'Python'))
