def duplicar(num):
    num = num * 2
    return num

duplicado = duplicar(3)
print(duplicado)

# simplificando la función
def duplicar(num):
    return num * 2

duplicado = duplicar(3)
print(duplicado)

# funciones lambda o anónimas con el parámetro num y luego lo que se quiere ejecutar
# como no tiene nombre, no es posible llamar a la función, entonces se la asigna a una variable
duplicado2 = lambda num: num * 2
print(duplicado2(3)) # () porque es una función para pasar el parámetro.

#otro ejemplo de compración con lambda

def suma(num1, num2):
    return num1 + num2

valor_sumado = suma(1, 2)
print(valor_sumado)

valor_sumado = lambda num1, num2: num1 + num2
print(valor_sumado(1, 2))

# otro ejemplo de compración para mostrar un mensaje
def mostrar_mje(mensaje):
    return f'Tu mensaje es: {mensaje}'

mje_mostardo = mostrar_mje('Hola')
print(mje_mostardo)

mje_mostardo = lambda mensaje: f'Tu mensaje es: {mensaje}'

print(mje_mostardo('Hola'))

# booleano

def numero_par(num):
    return num % 2 == 0

es_par = numero_par(2)
print(es_par)

es_par = lambda num : num % 2 == 0
print(es_par(2))
