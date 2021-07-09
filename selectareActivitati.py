from operator import itemgetter

"""
Se da o lista de activitati reprezentata prin perechile
(momentul de start, momentul de sfarsit).

Sa se aleaga din aceasta lista un numar maxim de activitati
pe care le poate efectua o persoana.

[ (9,12), (10,12), (9,10)]

Solutia: se aleg activitatile care au momentul de sfarsit cel mai mic


"""

def citireActivitati():
    result = []
    with open("input.txt") as file:
        for line in file:
            activity = tuple(int (x) for x in line.split())
            result.append(activity)
    return result


activitati = citireActivitati()
activitati.sort(key=itemgetter(1))

momentCurent = 0
solution = []
for x in activitati:
    if x[0] >= momentCurent:
        momentCurent = x[1]
        solution.append(x)

print(solution)