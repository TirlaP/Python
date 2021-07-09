
meniu = {1: "\n#_______________________________________________________#\n"
            "|\t1. Citeste date de la tastatura \t\t\t\t\t|\n",
         2: "|\t2. Citeste date din fisier \t\t\t\t\t\t\t|\n",
         3: "|\t3. Afiseaza matricea drumurilor \t\t\t\t\t|\n",
         4: "|\t4. Rezolva problema \t\t\t\t\t\t\t\t|\n",
         5: "|\t5. Info autor \t\t\t\t\t\t\t\t\t\t|\n",
         6: "|\t6. Termina program\t\t\t\t\t\t\t\t\t|\n"
          "#_______________________________________________________#\n"}

def introduDateTastatura():
    n = int(input('Introdu numarul de poduri: '))
    concurenti = []
    x = [0] * n
    for i in range(n):
        rivali = [int(a) for a in input("Rivalii firmei "+str(i)+" sunt ").split()]
        concurenti.append(rivali)
    return n, concurenti

def introduDateFisier():
    pod = []
    f = open('input.txt', 'r')
    n = int(f.readline())
    ins_start = int(f.readline())
    for i in range(n):
        ins = [int(x) for x in f.readline().split()]
        pod.append(ins)
    f.close()
    return n, ins_start, pod


def organizare(insula_crt, k):
    global x, concurenti, n
    if n == k and x[0] :
        for i in range(n):
            if i != n - 1:
                print(x[i], ', ', end='')
            else:
                print(x[i])
    else:
        for i in range(n):
            if posibil(i, k, insula_crt):
                x[k] = i
                if insula_crt == pod[i][0]:
                    ins = pod[i][1]
                else:
                    ins = pod[i][0]
                organizare(ins, k+1)

def posibil(alfa, k, ins_crt):
    global x, concurenti
    for j in range(k):
        if x[j] == alfa:
            return False
    for j in range(k):
        if
    return pod[alfa][0] == ins_crt or pod[alfa][1] == ins_crt

def infoAutor():
    print("\nProgramul a fost realizat de catre Tirla Petru!")

n = 0
concurenti = []
x = []

for i in meniu:
    print(meniu[i], end = '')

option = input("Enter your option: ")

while option != '6':
    if option == '1':
        n, concurenti = introduDateTastatura()
        x = [0] * n
    elif option == '2':
        pass
    elif option == '3':
        for i in concurenti:
            print(i)
    elif option == '4':
        organizare(ins_start, 0)
    elif option == '5':
        infoAutor()
    else:
        print("Invalid option.")

    for i in meniu:
        print(meniu[i], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")