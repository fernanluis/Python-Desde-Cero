# listas
mi_lista = []
print(mi_lista)

mi_lista = [1, 2, 3, 4, 5, 6]
print(mi_lista)

# posiciones
mi_lista = [1, 2, 3, 4, 5, 6]
print(mi_lista[4])

# modificar elemento de la lista
mi_lista[1] = 0
print(mi_lista)

lista_estudiantes = ['Luis', 'Fernando', 'Rafael', 'Ana Clara']
print(lista_estudiantes[-1]) # último de la lista

# imprimir por rango desde la posición 1 hasta el 2
print(lista_estudiantes[1:3])

# desde el inicio hasta la posición 2
print(lista_estudiantes[:3])

# penúltimo de la lista
print(lista_estudiantes[1:-1])

# hasta el último de la lista
print(lista_estudiantes[1:])

lista_combinada = ['Luis', 1, 12.5, True, ]
print(lista_combinada)

# una lista dentro de otra lista y acceder a un elemento en específico
nueva_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nueva_lista[1][1])

nueva_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], lista_combinada]
print(nueva_lista)

# añadir un elemento
lista_combinada.append('Nuevo dato')
print(lista_combinada)

# añadir al inicio
lista_combinada.insert(0, 'Dato 1')
print(lista_combinada)

# eliminar el último elemento de la lista
lista_combinada.pop()
print(lista_combinada)

# eliminar posición específico
lista_combinada.pop(1)
print(lista_combinada)

# buscar y eliminar un elemento
lista_combinada.remove('Dato 1')
print(lista_combinada)

# para conocer cuántos elementos posee una lista
print(len(lista_combinada))

# contar cuántas veces se repite un elemento en una lista
lista_combinada = ['Luis', 1, 12.5, True, 'Luis']
print(lista_combinada.count('Luis'))

# buscar la posición de un elemento
lista_combinada = ['Luis', 1, 12.5, True, 'Luis']
print(lista_combinada.index(12.5))
