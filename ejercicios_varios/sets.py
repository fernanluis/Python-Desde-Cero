conjunto = set()
print(conjunto)

# para asignar valores al conjunto se utilizan los mismos sigos utilizados en los diccionarios.
conjunto = {1, 2, 3, 4, 5, 6, 7}
print(conjunto)

# para almacenar elementos se va a utilizar el siguiente método.
conjunto.add('p')
conjunto.add('A')
conjunto.add('Elemento nuevo')
# se agregan pero no se muestran en el orden en el que se van agregando.

print(conjunto)

# para comprobar que un elemento existe en el set
existe = 'p' in conjunto
print(existe)

# conversión de un conjunto a una lista
lista_convertida = list(conjunto)
lista_convertida.append(2)
conjunto.add(2)
print(lista_convertida)
print(conjunto)

# conversión de un texto a un conjunto
texto = 'Se convertirá a conjunto'
print(set(texto))

# eliminar elementos de un conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7}
conjunto.add('p')
conjunto.add('A')
conjunto.add('Elemento nuevo')
conjunto.discard(1)
print(conjunto)

# vaciar todo el conjunto completo
conjunto.clear()
print(conjunto)
