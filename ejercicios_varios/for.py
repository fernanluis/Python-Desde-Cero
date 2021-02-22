numeros = [1,2,3,4,5,6,7,8,9,10]

for variable in numeros:
    print(variable)

# recorrer una tupla
numeros = (1,2,3,4,5,6,7,8,9,10)

for variable in numeros:
    print(variable)
# también es posible recorrer un diccionario
numeros_telefonicos = {'Contacto 1': 2345234, 'Contacto 2': 2345236, 'Contacto 3':2343587 }

for variable in numeros_telefonicos:
    print(variable)
# para mostrar los valores
for clave, valor in numeros_telefonicos.items():
    print('La clave es: ' + str(clave) + 'y el valor es: ' + str(valor))

# recorridos de cadenas de texto
mensaje = 'Aprendiendo Python'

for var in mensaje:
    print(var)

# otro tipo de recorrido
for var in range(1,9):
    print(var)
