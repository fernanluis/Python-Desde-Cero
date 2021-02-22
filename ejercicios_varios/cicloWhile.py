contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1

# nuevo ejemplo
contador = 0
while True:
    contador = contador + 2
    if contador == 30:
        break # sin break se convierte en un ciclo infinito.
    else:
        print(contador)

print('El ciclo finaliza')

# usando continue
contador = 0
while True:
    contador = contador + 2
    if contador == 30:
        break # sin break se convierte en un ciclo infinito.
    elif contador == 28:
        print('Este número no se muestra')
        continue # detiene la iteración actual a diferencia del break que detiene todo el ciclo while
    else:
        print(contador)

print('El ciclo finaliza')

# nuevo ejercicio
letra = input('Ingrese una letra')

while letra != 'a':
    print('No se ingresó la letra a')
    letra = input('Ingrese nuevamente la letra')

print('Ingresaste la letra a, finalizó el ciclo')
