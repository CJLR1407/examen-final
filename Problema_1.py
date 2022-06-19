#pregunta1
import random

miLista = []
def almacenar():
    for i in range(10):
        miLista.append(random.randrange(1, 20))

    print("Lista inicial es: {}".format(miLista))
    return miLista

def noRepetidos():
    miLista = almacenar()
    resultantList = []
    for element in miLista:
        if element not in resultantList:
            resultantList.append(element)

    return resultantList



item2 = []
listaDesc = []
resultantList = noRepetidos()
item2 =resultantList.copy()
item2.sort()

listaDesc =resultantList.copy()
listaDesc.sort(reverse=True)
print("Lista Ordenada Ascedente: ", item2)
print("Lista Ordenada Ascedente: ", listaDesc)


listadosNumero = [int(num) for num in item2]
print ("El numero mayor de la lista de item2 es : ",max(listadosNumero))