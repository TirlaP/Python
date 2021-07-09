#4 seturi de date

#matricea de 9 x 9 sa nu fie preluata element cu element de la tastatura
#ci sa cititi linie intreaga

#preia de la tastatura doar poz elementelor ocupate si valoarea lor

import citMatFis as cf
from time import time

meniu = {1: "\n#_______________________________________________________#\n"
            "|\t1. Citeste date de la tastatura \t\t\t\t\t|\n",
         2: "|\t2. Citeste date din fisier \t\t\t\t\t\t\t|\n",
         3: "|\t3. Afiseaza matricea drumurilor \t\t\t\t\t|\n",
         4: "|\t4. Rezolva problema \t\t\t\t\t\t\t\t|\n",
         5: "|\t5. Info autor \t\t\t\t\t\t\t\t\t\t|\n",
         6: "|\t6. Termina program\t\t\t\t\t\t\t\t\t|\n"
          "#_______________________________________________________#\n"}

def rezolva():
    coord=[0,0]
    if gaseste_liber(coord)==False:
        return True # rezolvare gata
    else:
        i, j = coord
        for nr in range(1,10):
            if Posibil(i, j, nr):
                mat[i][j] = nr
                if rezolva():
                    return True
                mat[i][j] = 0
        return False

def gaseste_liber(t):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                t[0], t[1] = i, j
                return True
    return False

def Posibil(nlin, ncol, nr):
    return posibil_linie(nlin, nr) and \
        posibil_coloana(ncol, nr) and \
        posibil_caseta(nlin, ncol, nr)

def posibil_linie(nlin, nr):
    for j in range(9):
        if mat[nlin][j] == nr:
            return False
    return True
#
def posibil_coloana(ncol, nr):
    for i in range(9):
        if mat[i][ncol] == nr:
            return False
    return True
#
def posibil_caseta(nlin, ncol, nr):
    i0 = nlin - nlin % 3
    j0 = ncol - ncol % 3
    for di in range(3):
        for dj in range(3):
            if mat[i0+di][j0+dj] == nr:
                return False
    return True

mat = []
f = open('input.txt', 'r')
# mat = cf.citesteMatrice("exsudoku1.txt", sep=',')
mat = cf.citesteMatrice(f)

t0 = time()
if rezolva():
    print("Solutia", end='')
else:
    print("Nu s-a gasit nici o solutie", end='')
print(' (%.3f s)' % (time() - t0))
print(' (%.3f s)' % (time() - t0))
for i in range(9):
    print(mat[i])


for opt in meniu:
    print(meniu[opt], end='')
optiune = int(input('Introdu optiunea dorita: '))

while (optiune != 5):
    if optiune == 1:
        # mat = cf.citesteMatrice("exsudoku1.txt", sep=',')
        mat = cf.citesteMatrice(f)
    elif optiune == 2:
        t0 = time()
        if rezolva():
            print("Solutia", end='')
        else:
            print("Nu s-a gasit nici o solutie", end='')
        print(' (%.3f s)' % (time() - t0))
    elif optiune == 3:
        for i in range(9):
            print(mat[i])
    elif optiune == 4:
        #info autor
        pass

    for opt in meniu:
        print(meniu[opt], end = '')
    optiune = int(input('Introdu optiunea dorita: '))
