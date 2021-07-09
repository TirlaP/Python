import math

meniu = {1: "\n#_______________________________________________________#\n"
            "|\t1. Citirea polinomului din fisier \t\t\t\t\t|\n",
         2: "|\t2. Afisarea polinomului citit \t\t\t\t\t\t|\n",
         3: "|\t3. Calculul valorii polinomului in punctul X \t\t|\n",
         4: "|\t4. Modificarea unui monom din polinom* \t\t\t\t|\n",
         5: "|\t5. Info autor \t\t\t\t\t\t\t\t\t\t|\n",
         6: "|\t6. Termina program\t\t\t\t\t\t\t\t\t|\n"
          "#_______________________________________________________#\n"}

def citirePolinom(list_monom, list_coeficienti):
    with open('input.txt') as f:
        linii = f.readlines()
        list_monom = linii[0].split(' ')
        list_coeficienti = linii[1].split(' ')

    return list_monom, list_coeficienti

def afisarePolinom(list_monom, list_coeficienti):
    print('P(x) = ', end='')
    for x in range(len(list_coeficienti)):
        if x == 0:
            print(str(list_coeficienti[x])+'+',end='')
        elif x == len(list_coeficienti) - 1:
            print(str(list_coeficienti[x])+'*X^'+str(list_monom[x]), end='')
        else:
            print(str(list_coeficienti[x])+'*X^'+str(list_monom[x])+'+', end='')

def calcularePolinomX(list_monom, list_coeficienti):
    x = int(input('Introdu valoarea in care vrei sa calculezi polinomul: '))
    rez = 0

    for i in range(len(list_coeficienti)):
        rez += int(list_coeficienti[i]) * math.pow(x, int(list_monom[i]))

    print(f'Valoarea polinomului in punxtul {x} = ', rez)

def modificareMonomPolinom(list_monom, list_coeficienti):
    grad_monom = input('Dati gradul monomului: ')
    coeficient = input('Dati coeficientul monomului: ')

    for x in range(len(list_coeficienti)):
        if list_monom[x] == grad_monom:
            list_coeficienti[x] = coeficient
            break

    return list_coeficienti

def infoAutor():
    print('Programul a fost creat de catre Tirla Petru din grupa 3112A')

list_monom = []
list_coeficienti = []

for x in meniu:
    print(meniu[x], end = '')

option = input("Enter your option: ")

while option != '6':
    if option == '1':
        list_monom, list_coeficienti = citirePolinom(list_monom, list_coeficienti)
    elif option == '2':
        afisarePolinom(list_monom, list_coeficienti)
    elif option == '3':
        calcularePolinomX(list_monom, list_coeficienti)
    elif option == '4':
        modificareMonomPolinom(list_monom, list_coeficienti)
    elif option == '5':
        infoAutor()
    else:
        print("Invalid option.")

    for x in meniu:
        print(meniu[x], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")

'Impacat cu mine.'
# Cristian Cuciureanu
# Ramona Tiepac