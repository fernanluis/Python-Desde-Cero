# Secuencia de datos

# list - Lista, o secuencia de valores cambiantes
# tuple - Tupla, o secuencia de valores inmutable
# set - Colección de valores únicos
# dict - Diccionario, o colección de pares de clave-valor

# Cadenas, Ordenables SI, Mutable NO
# Las listas son creadas usando corchetes y comas
name = "Luis Fernando Ramos"

print(name[0])
print(name[4])

# Listas, Ordenables SI, Mutables SI

# append - agregar elementos a una lista al final de la lista

# sort - ordenar una lista

names = ["Harry", "Ron", "Hermione"]
# Imprimir toda la lista:
print(names)
# Imprimir el segundo elemento de la lista:
print(names[1])
# Agregar un nombre al final de la lista:
names.append("Draco")
print(names)
# Ordenar la lista:
names.sort()
# Imprimir la nueva lista:
print(names)

# Tuplas, Ordenable SI, Mutable SI
# Las Tuplas se utilizan generalmente cuando necesitamos almacenar solo dos o tres variables,
# como los valores x e y para un punto en un plano. En el código Python se usan paréntesis.

point = (12.5, 10.6)

# Set, Ordenable NO, Mutable NO APLICA
# Los conuntos o set se diferencian de las listas y tuplas en que no estan ordenados.
# También son diferentes porque, si bien podemos tener dos o más elementos iguales de una
# lista / tupla, un set solo almacenará cada valor una vez.
# Podemos definir un set vacío usando la función set. Luego podemos usar agregar y quitar para
# agregar y quitar elementos de ese conjunto, y la función len para encontrar el tamaño del conjunto.
# Tener encuenta que la función len funciona en todas las secuencias en Python. También
# ten en cuenta que a pesar de agregar 4 y 3 al conjunto dos veces, cada elemento solo puede aparecer una vez en un conjunto.

# Crear un conjunto (set) vacío:
conjunto = set()
print(conjunto)

conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add(4)
conjunto.add(3)
conjunto.add(1)
print(conjunto)

# Remover 2 elementos del set
conjunto.remove(2)
# Imprimir el set:
print(conjunto)

# Encontrar el tamaño del set
print(f"El set tiene {len(conjunto)} elementos.")

# Diccionarios. Ordenable NO, Mutable SI.
# Un diccionario es un conjunto de pares clave-valor (key-value), donde cada clave tiene un valor
# correspondiente.
# En Python,usamos las llaves para para contener un diccionario y dos puntos para indicar claves y valores.

# Definir un diccionario
casas = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Imprimir la casa de Harry
print(casas["Harry"])
# Agregar valores a un diccionario:
casas["Hermione"] = "Gryffindor"
# Imprimir la casa de Hermione:
print(casas["Hermione"])
print(casas)
