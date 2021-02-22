# sistema de archivos
archivo = open('archivo.txt', 'r') # abrir archivo con permisos de lectura
print(archivo.read()) # leer el archivo
archivo.close()# cerrar el archivo
print('Se ha abierto, leído y cerrado el archivo')

# para solo una línea
archivo = open('archivo.txt', 'r') # abrir archivo con permisos de lectura
print(archivo.readline()) # leer el archivo de una sola línea
archivo.close()# cerrar el archivo
print('Se ha abierto, leído una sola línea y cerrado el archivo')

#para recorrer todas las líneas de un archivo
archivo = open('archivo.txt', 'r') # abrir archivo con permisos de lectura
for linea in archivo:
    print(linea, end='') # para evitar el salto de línea
archivo.close()# cerrar el archivo
print('Se esan recorriendo cada una de las líneas con un ciclo for')

# escribir en el archivo
# archivo = open('archivo.txt', 'w') # abrir archivo con permisos de lectura
archivo = open('archivo.txt', 'a')
archivo.write('\nTexto desde cero') # 'w' sobreescribe la información anterior
archivo.close()# cerrar el archivo
print('Se está escribiendo el archivo')

# ciclo for para añadir múltiples líneas
archivo = open('archivo.txt', 'w') # sobreescribe todo lo anterior
for linea in range(1, 11):
    archivo.write('\nTexto ' + str(linea))
archivo.close()# cerrar el archivo
print('Se están añadiendo múltiples líneas')
