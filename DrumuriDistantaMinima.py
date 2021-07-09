"""
Algoritmul lui Dijkstra

S-a atribuit inf = float('inf'), "infinit"

localitati = ['Sv', 'Rd', 'Putna', 'Mg', 'Sucv', 'G-H', 'Vor']
manastiri = [
[0, 37, inf, inf, inf, 35, inf], #Sv
[37, 0, 30, 9, inf, inf, inf],   #Rd
[inf, 30, 0, 25, inf, inf, inf], #Putna
[inf, 9, 25, 0, 9, 25, inf],     #Mg
[inf, inf, inf, 9, 0, inf, inf], #Sucv
[35, inf, inf, 25, inf, 0, 4],   #G-H
[inf, inf, inf, inf, inf, 4, 0]  #Vor
]

Se utilizeaza 3 liste:

1. dist[] - memoram distantele minime dintre nodul sursa si celelalte n-1 noduri

2. prec[] - memoram 'tatii', predecesorii directi ai fiecarui nod

3. q[] - lista populata la inceput cu toate nodurile, din care va fi extras,
        rand pe rand, cate un nod aflat la distanta minima fata de nodul de start

"""

inf = float('inf')

def Dijkstra (G, start):
    n = len(G)
    dist = [inf] * n
    prec = [None] * n
    dist[start] = 0
    q = [nod for nod in range(n)]

    while q:
        nodMin = nod_q_min_dist(q, dist)
        q.remove(nodMin)
        if dist[nodMin] == inf:
            break
        for v in vecini_in_q(nodMin, q, G):
            dv = dist[nodMin] + G[nodMin][v]
            if dv < dist[v]:
                dist[v] = dv
                prec[v] = nodMin
    return dist, prec

def nod_q_min_dist(q, dist):
    dmin = inf
    for nod in q:
        if dist[nod] <= dmin:
            dmin = dist[nod]
            nodMin = nod
    return nodMin

def vecini_in_q(u, q, G):
    vecini = []
    for x in q:
        if G[u][x] < inf:
            vecini.append(x)
    return vecini

def fnum(x):
    return str(x + 1)

def afisSolutie(nodStart, d, prec, fden = fnum, afis_d_prec = True):
    if afis_d_prec:
        print("dist = ", d)
        print("prec = ", prec)
    print('De la nodul ', fden(nodStart), 'distanta minima la celelalte noduri:')
    for x in range(len(d)):
        print(fden(x), '. d = ', d[x], ' : ', sep = '', end = '')
        afisareCale(x, prec, fden)

def afisareCale(nod, prec, fden = fnum):
    s = []
    while nod != None:
        s.append(nod)
        nod = prec[nod]
    s.reverse()
    print("->".join( list (map(fden, s) )))

if __name__ == '__main__':
    print('Exemplul manastiri din Bucovina')
    localitati = ['Sv', 'Rd', 'Putna', 'Mg', 'Sucv', 'G-H', 'Vor']
    manastiri = [
        [0, 37, inf, inf, inf, 35, inf],  # Sv
        [37, 0, 30, 9, inf, inf, inf],    # Rd
        [inf, 30, 0, 25, inf, inf, inf],  # Putna
        [inf, 9, 25, 0, 9, 25, inf],      # Mg
        [inf, inf, inf, 9, 0, inf, inf],  # Sucv
        [35, inf, inf, 25, inf, 0, 4],    # G-H
        [inf, inf, inf, inf, inf, 4, 0]   # Vor
    ]

    def denLoc(x):
        return localitati[x]

    plecare = localitati.index('Sv')
    d, prec = Dijkstra(manastiri, plecare)
    afisSolutie(plecare, d, prec, denLoc)