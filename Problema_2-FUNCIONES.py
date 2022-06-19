
import random
import math

def lista(filename):
    tamanio = int(input("Ingrese el tamaño de la lista"))
    cantidad = int(input("Cuantos numeros va ingresar? "))
    lista = []

    for a in range(0, cantidad):
        b = int(input("Ingrese su numero "))
        lista.append(b)

    for num in range(0, tamanio):
        if lista[num] == "":
            lista.insert(num, random.randrange(1, 20))

    file = open(filename, "a+")
    for n in range(len(lista))
        file.write("\n{}".format(lista[n]))
    file.close()
    return

def raiz(filename):
    file = open(filename, "r")
    file.readline()

    file.write("\n{}".format(lista))
    file.close()
