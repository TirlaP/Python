from operator import itemgetter

lista_activitati=[ (9,12), (10,12), (9,10)]
lista_activitati.sort(key = itemgetter(1))

print(lista_activitati)

def parcurgeLista(lista_activitati):
    for x, y in lista_activitati:
        pass