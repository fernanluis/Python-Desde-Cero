import sys
try:
    numero1 = int(input("Ingrese primer numero: "))
    numero2 = int(input("Ingrese segundo numero: "))
except ValueError:
    print("Error: Valor no valido. ")
    sys.exit(1)
try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")
    #Salir del programa
    sys.exit(1)

print(f"{numero1} / {numero2} = {resultado}")

#ELSE
# Puedes usar la palabra clave else para definir un bloque de código
# que se ejecutará si no se produjeron errores:

try:
    print("Hola")
except:
    print("Algo salió mal")
else:
    print("Nada salió mal")


# FINALLY
# El bloque finally, si se especifica, se ejecutará independientemente
# de si el bloque try genera un error o no.
try:
    print("Hola")
except:
    print("Algo salió mal")
finally:
    print("El try y except finalizó")
