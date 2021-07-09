"""
Metoda Greedy

Este data o multime A si se cere sa se gaseasca o submultime B
care sa indeplineasca anumite conditii.

Aceasta metoda nu isi propune gasirea celei mai bune solutii, ci 
a uneia dintre ele care indeplineste criteriul de optimizare ales.


Mecanism general:

1. Se initializeaza multimea solutiilor cu multimea vida
2. Se alege un element x din multimea A
3. Se verifica daca un element ales poate fi adaugat la multimea solutiilor,
daca da atunci va fi adaugat: B = B U {x}
4. Se continua repetitiv cu pasul 2 pana cand au fost determinate toate
elementele din multimea solutiilor

Pseudocod:

procedura Greedy_1(A, n, B) este
    B = 0
    pentru i = 1, n executa
        x = ALEGE(A, n, i)
        daca POSIBIL(B, x) atunci
            ADAUG(B, x)
        @
    @
sfarsit

"""

"""
procedura Bancomat(bancnote, n, solutie) este
    solutie = 0
    pentru i = 1, n executa
        choice = ALEGE(bancnote, n, i)
        daca POSIBIL(solutie, choice) atunci
            ADAUG(solutie, choice)
        @
    @
sfarsit
"""

def Bancomat(suma, bancnote, afis = True):
    bancnote.sort(reverse = True)
    if afis:
        print("Suma = ", suma, "Bancnote disponibile: ", bancnote)
    rez = []
    while(suma > 0):
        if len(bancnote) == 0:
            break
        if suma >= bancnote[0]:
            nr_bancnote = suma // bancnote[0]
            suma = suma % bancnote[0]
            rez.append([bancnote[0], nr_bancnote])
        bancnote.pop(0)
    else:
        return rez
    return []

def citireBancnoteFisier():
    rez = []
    with open("input.txt", 'rt') as file:
        for line in file:
            campuri = [int (x) for x in line.split(',')]
            rez.append(campuri)
    return rez


def bancomatLimitat(suma, bancnote, afis = True):
    bancnote.sort(reverse = True)
    if afis:
        print("Suma = ", suma, "Bancnote disponibile: ", bancnote)
    rez = []
    i = 0
    while suma > 0:
        if len(bancnote) == 0:
            break
        if (suma >= bancnote[i][0] and bancnote[i][1] > 0):
            nr_bancnote = suma // bancnote[i][0]
            bancnote[i][1] -= nr_bancnote
            suma = suma % bancnote[i][0]
            rez.append([bancnote[i][0], nr_bancnote])
        i += 1
    else:
        return rez
    return []


def livrare(pachet):
    if len(pachet) == 0:
        print("Nu dispunem de bancnotele necesare")
    else:
        for val, nr in pachet:
            print(nr, "x", val, "lei", end='   ')
        print()



suma = 300
bancnote = citireBancnoteFisier()
pachetLivrare = bancomatLimitat(suma, bancnote)
livrare(pachetLivrare)
print(bancnote)
print()