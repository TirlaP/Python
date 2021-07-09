
def citire_tastatura():
    n = int(input("Dati numarul de linii si coloane:"))
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        mat[i] = [int(x) for x in input("Elementele de pe linia " + str(i) + ":").split()]

    m = int(input("Dati dimensiunea submatricilor:"))
    while(m >= n):
        print("\nDimensiunea submatricilor este invalida. Trebuie sa fie mai mica decat cea a matricei. Incercati din nou!")
        m = int(input("\nDati dimensiunea submatricilor:"))

    return mat, m

def citire_fisier(numeFisier):
    f = open(numeFisier, "r")

    n = int(f.readline())
    m = int(f.readline())
    mat = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        mat[i] = [int(x) for x in f.readline().split()]

    f.close()

    return mat, m

def afisare_matrice(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()

def calculeaza_sume(mat, m):
    n = len(mat)
    sum = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sumaCurenta = 0
            k = i
            while k < i + m:
                l = j
                while l < j + m:
                    sumaCurenta += mat[k][l]
                    l += 1
                k += 1
            sum.append(sumaCurenta)
    return sum


numeFisier = "input.txt"
mat, m = citire_fisier(numeFisier)

sum = calculeaza_sume(mat, m)
print("\nSumele submatricilor sunt: ", end="")
for i in sum:
    print(i, end= " ")
print('\n')

print("Matricea este: ")
afisare_matrice(mat)
print()

# Afisati pe ecran continutul unei matrici citite dintr-un fisier parcurgand matricea in spirala

def afisare_matrice_spirala(mat):
    n = len(mat[0])
    # pentru toate cadranele matricei
    for i in range(n//2):

        # latura de sus
        j = i
        while j < n - i:
            print(mat[i][j], end=" ")
            j += 1

        # latura din dreapta
        j = i + 1
        while j < n - i:
            print(mat[j][n - i - 1], end=" ")
            j += 1

        # latura de jos
        j = n - i - 2
        while j >= i + 1:
            print(mat[n - i - 1][j], end=" ")
            j -= 1

        # latura din stanga
        j = n - i - 1
        while j >= i + 1:
            print(mat[j][i], end=" ")
            j -= 1

    # in caz ca dimensiunea matricei este impara
    if n % 2 == 1:
        print(mat[n//2][n//2])

afisare_matrice_spirala(mat)