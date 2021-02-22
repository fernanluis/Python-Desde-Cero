numero1 = 9
numero2 = 1

suma = numero1 + numero2
# print('El resultado es: ' suma) esto da error
# print solo acepta concatenaciones de tipo string

# para convertilo el valor entero a string hcaer lo siguiente.
print('El resultado es: ' + str(suma))
print(type(suma))

# conversión de tipo decimal a string
numero_decimal = 1.2
print('El resultado es: ' + str(numero_decimal))
print(type(numero_decimal))

numero_decimal = str(1.2)
print(type(numero_decimal))

booleano = str(True)
print(type(booleano))

numero_entero = 5
texto = '2.4'
print(type(numero_entero), type(texto))

numero_entero = float(6)
texto = float('2.4')
print(type(numero_entero), type(texto))

numero_decimal = 2.7
texto = '5'
print(type(numero_decimal), type(texto))

numero_decimal = int(2.7)
texto = int('5')
print(type(numero_decimal), type(texto))

print(bool(0), bool(''), bool('Hola'), bool(-3.5))

# no es posible convertir un texto a entero. Tampoco a flotante de un tipo texto.
