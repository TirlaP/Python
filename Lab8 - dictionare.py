import math
meniu = {1: "\n#_______________________________________________________#\n"
            "|\t1. Citirea polinomului din fisier \t\t\t\t\t|\n",
         2: "|\t2. Afisarea polinomului citit \t\t\t\t\t\t|\n",
         3: "|\t3. Calculul valorii polinomului in punctul X \t\t|\n",
         4: "|\t4. Modificarea unui monom din polinom* \t\t\t\t|\n",
         5: "|\t5. Info autor \t\t\t\t\t\t\t\t\t\t|\n",
         6: "|\t6. Termina program\t\t\t\t\t\t\t\t\t|\n"
          "#_______________________________________________________#\n"}

def citirePolinom(dict_polinom):
    cnt = 0
    with open('input.txt') as f:
        linii = f.readlines()
        list_monom = [float(x) for x in linii[0].split()]
        list_coeficienti = [int(x) for x in linii[1].split()]
        for x in list_monom:
            dict_polinom[x] = list_coeficienti[cnt]
            cnt += 1

    return dict_polinom

def afisarePolinom(dict_polinom):
    print('P(x) = ', end='')
    for x in dict_polinom:
        if x == 0:
            print(str(dict_polinom[x])+'+',end='')
        elif x == len(dict_polinom)-1:
            print(str(dict_polinom[x])+'*X^'+str(x)+'+', end='')
        else:
            print(str(dict_polinom[x])+'*X^'+str(x)+'+', end='')

def calcularePolinomX(dict_polinom):
    x = int(input('Introdu valoarea in care vrei sa calculezi polinomul: '))
    rez = 0

    for i in dict_polinom:
        rez += int(dict_polinom[i]) * math.pow(x, int(i))

    print(f'Valoarea polinomului in punxtul {x} = ', rez)

def modificareMonomPolinom(dict_polinom):
    grad_monom = float(input('Dati gradul monomului: '))
    grad_monom_nou = float(input('Dati gradul nou al monomului: '))
    coeficient = int(input('Dati coeficientul monomului: '))

    ok = 0
    for x in dict_polinom:
        if x == grad_monom:
            dict_polinom[grad_monom_nou] = dict_polinom.pop(x)
            dict_polinom[grad_monom_nou] = coeficient
            ok = 1
            break

    if ok == 0:
        dict_polinom[grad_monom_nou]= coeficient

    ordered = dict(sorted(dict_polinom.items()))

    return ordered

def infoAutor():
    print('Programul a fost creat de catre Tirla Petru din grupa 3112A')

dict_polinom = {}

for x in meniu:
    print(meniu[x], end = '')

option = input("Enter your option: ")

while option != '6':
    if option == '1':
        dict_polinom = citirePolinom(dict_polinom)
    elif option == '2':
        afisarePolinom(dict_polinom)
    elif option == '3':
        calcularePolinomX(dict_polinom)
    elif option == '4':
        dict_polinom = modificareMonomPolinom(dict_polinom)
    elif option == '5':
        infoAutor()
    else:
        print("Invalid option.")

    for x in meniu:
        print(meniu[x], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")

