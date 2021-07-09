
def bancomat (suma, bancnote, afis = True):
    bancnote.sort(reverse = True)
    if afis:
        print("Suma = ", suma, "Bancnote disponibile:", bancnote)
    rez = []
    while (suma > 0):
        if len(bancnote) == 0:
            break
        if (suma >= bancnote[0]):
            nr_bancnote = suma // bancnote[0]
            suma = suma % bancnote[0]
            rez.append([bancnote[0], nr_bancnote])
        bancnote.pop(0)
    else:
        return rez
    return []

def livrare (pachet):
    if len(pachet)==0:
        print("Nu dispunem de bancnotele necesare")
    else:
        for val, nr in pachet:
            print(nr, "x", val, "lei", end = '   ')
        print()

def bancomatLimitat():
    pass

pachetLivrare = bancomat(73, [50, 10, 5, 1])
print("Rezultat bancomar(): ", pachetLivrare)
livrare(pachetLivrare)
print()

bnk = [100,50,10,5]
livrare(bancomat(1075, bnk))
print()

s = 170
print("Suma", s)
livrare(bancomat(s, bnk, afis = False))
print("Explicati!")
print()

livrare(bancomat(25, [5,1]))
print()

livrare(bancomat(10, [1]))
print()
livrare(bancomat(87, [50, 10, 5]))