
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
    ins_start = int(input('Introdu insula de pornire: '))
    pod = []
    x = [0] * n
    for i in range(n):
        ins = [int(a) for a in input("Podul nr. "+str(i)+" este intre insulele ").split()]
        pod.append(ins)
    return n, ins_start, pod

def introduDateFisier():
    nrSeturi = 0
    pod = []
    n = 0
    ins_start = 0

    f = open('input.txt', 'r')
    while nrSeturi < 2:
        nrSeturi += 1
        newN = int(f.readline())
        ins_start = int(f.readline())
        for j in range(newN):
            ins = [int(x) for x in f.readline().split()]
            pod.append(ins)
        n += newN

    print(n)
    print(pod)

    return n, ins_start, pod


def plimbare(insula_crt, k):
    global x, pod, n, nrSol
    if n == k:
        nrSol += 1
        for i in range(n):
            if i != n - 1:
                print(x[i], ', ', end='')
            else:
                print(x[i])
    else:
        for alfa in range(n):
            if posibil(alfa, k, insula_crt):
                x[k] = alfa
                if insula_crt == pod[alfa][0]:
                    ins = pod[alfa][1]
                else:
                    ins = pod[alfa][0]
                plimbare(ins, k+1)

def posibil(alfa, k, ins_crt):
    global x, pod
    for j in range(k):
        if x[j] == alfa:
            return False
    return pod[alfa][0] == ins_crt or pod[alfa][1] == ins_crt

def infoAutor():
    print("\nProgramul a fost realizat de catre Tirla Petru!")

n = 0
nrSol = 0
ins_start = 0
pod = []
x = []

for i in meniu:
    print(meniu[i], end = '')

option = input("Enter your option: ")

while option != '6':
    if option == '1':
        n, ins_start, pod = introduDateTastatura()
        x = [0] * n
    elif option == '2':
        n, ins_start, pod = introduDateFisier()
        x = [0] * n
    elif option == '3':
        for i in pod:
            print(i)
    elif option == '4':
        plimbare(ins_start, 0)
        if nrSol == 0:
            print("\n* Nu exista solutie")
        else:
            print(f"\n* Numarul de solutii este de {nrSol}")
    elif option == '5':
        infoAutor()
    else:
        print("Invalid option.")

    for i in meniu:
        print(meniu[i], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")