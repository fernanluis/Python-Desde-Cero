nombre_curso = 'Python'

print('Bienvenido al curso de ' + nombre_curso)

nombre_curso = 'JavaScript'

print('Bienvenido al curso de ' + nombre_curso)

nombre_curso = input('Ingrese el nombre del curso: ')
print('Bienvenido al curso de ' + nombre_curso)

curso1 = curso2 = 'Python'
print(curso1)
print(curso2)

estudiante1, estudiante2, estudiante3 = 'Luis', 'Fernando', 'Pablo' # los calores asignados deben ser tanto como variables se quieren definir.
print(estudiante1, estudiante2, estudiante3)

# trbajando con format
mensaje = 'Aprender Python es fácil'
print('El valor de mi variables es: ' + mensaje)

print('El valor de mi variables es: {}'.format(mensaje))

# texto con formato 'f'
print(f'El valor de mi variables es: {mensaje}')
