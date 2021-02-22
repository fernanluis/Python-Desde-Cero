mi_diccionario = {} # diccionario vacío
print(type(mi_diccionario))

#para añadir datos a un diccionarios clave_valor
diccionario_traducción =  {'hola': 'hello', 'rojo':'red', 'libro':'book'}
print(diccionario_traducción)

# modificar algún elemento del diccionario se puede acceder a él mediante su clave.
diccionario_traducción['rojo'] = 'blue'
print(diccionario_traducción)

#para eliminar
del(diccionario_traducción['libro'])
print(diccionario_traducción)

# nuevo diccionario
estudiante =  {
    'Nombre': 'Luis',
    'Apellido':'Ramos',
    'Edad':23,
    'Curso':'Python'
    }

print(estudiante)

# diccionario dentro del diccionario
estudiante =  {
    'Nombre': 'Luis',
    'Apellido':'Ramos',
    'Edad':23,
    'Curso': {'nombre_curso': 'Python', 'Nivel': 'Básico'}
    }

print(estudiante)

# listas dentro de un diccionario dentro de un diccionario

estudiante1 =  {
    'Nombre': 'Luis',
    'Apellido':'Ramos',
    'Edad':23,
    'Curso':[
        {'nombre_curso': 'Python', 'Nivel': 'Básico'},
        {'nombre_curso': 'JavaScript', 'Nivel': 'Medio'},
        {'nombre_curso': 'Php', 'Nivel': 'Avanzado'},
    ]
    }

estudiante2 =  {
    'Nombre': 'Fernando',
    'Apellido':'Lunguni',
    'Edad':24,
    'Curso':[
        {'nombre_curso': 'Python', 'Nivel': 'Básico'},
        {'nombre_curso': 'JavaScript', 'Nivel': 'Medio'},
        {'nombre_curso': 'Php', 'Nivel': 'Avanzado'},
    ]
    }

estudiantes = []
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
print(estudiantes)

# Para verel nombre del primer estudiante pero mediante la lista no del diccionario.
print(estudiantes[0]['Nombre'])
