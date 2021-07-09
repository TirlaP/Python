from operator import *

# citeste pret, volum din fisier
# p[i], v[i] vectori indexati de la
# ordoneaza obiectele in functie de raportul p/v
# x vectorul solutie

'''
def citireDate(list_volum, list_pret):
    with open('input.txt') as f:
        linii = f.readlines()
        list_volum = linii[0].split(' ')
        list_pret = linii[1].split(' ')

    return list_volum, list_pret

def listaObiecte (list_volum, list_pret, dict_o):
    for x in range(len(list_volum)):
        dict_o[list_volum[x]] = [list_pret[x]]
    return dict_o
'''

def afisareDate(list_volum, list_pret, dict_o):
    for x in range(len(dict_o)):
        print(dict_o[x])

dict_o={}
list_volum = []
list_pret = []
n = int(input('Introdu numarul de obiecte: '))
for i in range(n):
    p = int(input('pret:'))
    list_pret.append(p)
    v = int(input('volum:'))
    list_volum.append(v)
    dict_o[p/v]= [p,v]
print(dict_o)

sorted_items = sorted(dict_o.items(),reverse=True)
print(sorted_items)

for i in sorted_items:
    print(sorted_items[i][1])

print()

vt = pt = 0
V = 15
sol = []
i = 0

while vt < V and i < n:
    if vt + sorted_items[i][1] <= V:
        sol.append(1)
        pt = pt + sorted_items[i][0]
        vt = vt + sorted_items[i][1]
    else:
        sol.append((V - vt)/sorted_items[i][1])
        vt = V
        pt = pt + sorted_items[i][0] * sol[i]
    i += 1

print("Pretul total al obiectelor din rucsac = ", pt, "Volumul ocupat = ", vt)
print("In rucsac s-au introdus:")
for i in range(n):
    if (sol[i] > 0):
        print("-obiectul ", i+1, "(", sorted_items[i][1]*sol[i], ",", sorted_items[i][0], ")")




