# FINALLY
# Ejemplo intentando abrir y escribir a un archivo que es de solo lectura:

try:
    f = open("arhivoejemplo.txt")
    f.write("Linea de prueba dentro del archivo.")
except:
    print("Algo pasó al intentar abrir el archivo.")
finally:
    f.close()
