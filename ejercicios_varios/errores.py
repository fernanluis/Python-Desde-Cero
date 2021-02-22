try:
    numero1 = input('Ingrese el número 1: ')
    numero2 = input('Ingrese el número 2: ')
    suma = int(numero1) + int(numero2)
    print(suma)
except:
    print('Ha ocurrido un error')

# otro ejercicio con cálculo de división
try:
    numero3 = input('Ingrese el primer número: ')
    numero4 = input('Ingrese el segundo número: ')
    division = int(numero3) / int(numero4)
    print(division)
except ZeroDivisionError:
    print('No se puede dividir para cero')
except:
    print('Ingrese los números correctos')
finally: # va a ejecutar el try, en caso de no suceder ningún error que no se ejecuten en ninguno de los except anteriores, al final de la ejecucioón va a ejecutar lo siguiente.
    print('Ha finalizado el programa')

# otro tipo de error
try:
    print(nombre)
except NameError:
    print('Debe declarar la variable')

# otro tipo de error.
try:
    numero = 2
    texto = 'Bienvenidos'
    suma = numero + texto
except TypeError:
    print('No se puede realizar la operación')

# almacenando en una variable el error encontrado
try:
    numero = 2
    texto = 'Bienvenidos'
    suma = numero + texto
except TypeError as error:
    print('El error es: ' + str(error))
