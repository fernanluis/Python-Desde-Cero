# Loops. Bucles
# 2 formas principales: for y while

# for se utiliza para iterar sobre una secuencia de elementos, realizando una tabulación
# o aumento del nivel de sangría en el bloque de código para cada elemento en una secuencia.

for i in [0, 1, 2, 3, 4, 5]:
    print (i)

# Podemos condensar este códgo usando la función rango de Python, que nos permite obtener
# fácilmente una secuencia de números.

for i in range (6):
    print(i)

# Loop con lista. imprimir cada nombre en una lista

# Crear una lista
nombres = ["Harry", "Ron", "Hermione"]
# Imprimir cada nombre
for unNombre in nombres:
    print(unNombre)

# Podemos recorrer cada carácter en un solo nombre.
nombre = "Harry"
for caracter in nombre:
    print(caracter)
