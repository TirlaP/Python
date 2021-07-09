meniu = {1: "\n#_______________________________________________________#\n"
            "|\t1. Incarcare informatii despre studenti \t\t\t|\n"
            "|\tde la tastatura \t\t\t\t\t\t\t\t\t|\n",
         2: "|\t2. Afisare studenti \t\t\t\t\t\t\t\t|\n",
         3: "|\t3. Afisare note \t\t\t\t\t\t\t\t\t|\n",
         4: "|\t4. Afisare studenti si notele obtinute \t\t\t\t|\n",
         5: "|\t5. Cautare student dupa nume \t\t\t\t\t\t|\n",
         6: "|\t6. Afisare studenti promovati\t\t\t\t\t\t|\n",
         7: "|\t7. Info autor \t\t\t\t\t\t\t\t\t\t|\n",
         8: "|\t8. Termina program\t\t\t\t\t\t\t\t\t|\n"
          "#_______________________________________________________#\n"}


def introduStudent(dict_stud, dict_note):
    with open('input.txt') as f:
        for linie in f.readlines():
            campuri = linie.split(',')
            id_s = int(campuri[0])
            lst_note = [int(x) for x in campuri[2].split()]
            dict_stud[id_s] = campuri[1]
            dict_note[id_s] = lst_note
    '''
    Citire de la tastatura
    linie_citita = input('Dati info despre student:')
    # print(linie_citita)
    campuri = linie_citita.split(',')
    # print(campuri)
    id_s = int(campuri[0])
    lst_note = [int(x) for x in campuri[2].split()]

    dict_stud[id_s] = campuri[1]
    dict_note[id_s] = lst_note
    '''
    return dict_stud, dict_note

def afisareStudenti(studenti):
    print("\nID\tNume student")
    for x in studenti:
        print(x, '\t', studenti[x])

def afisareNote(note):
    print("\nID\tNote")
    for x in note:
        print(x, end = '\t')
        for y in note[x]:
            print(y, end = ' ')
        print()

def afisareStudNote(studenti, note):
    print("\nID\tNume student\tNote\n",
          "_"*30)
    for x in studenti:
        print(x, '\t', studenti[x], end = '\t')
        for y in note[x]:
            print(y, end=' ')
        print()

def cautareStudent(studenti, note):
    ok = 0
    cautat = input("Introdu numele studentului cautat: ")
    for x in studenti:
        if cautat in studenti[x]:
            print("\nID\tNume student\tNote\n",
                  "___________________________________")
            print(x, '\t', studenti[x], end = '\t')
            for y in note[x]:
                print(y, end=' ')
            print()
            ok = 1
    if ok == 0:
        print("Studentul nu este in baza de date!")

def afisarePromovati(studenti, note):
    cnt = 0
    global dict_medie
    print("\nID\tNume student\tMedia\n",
          "___________________________________")
    for x in note:
        media = 0
        media = sum(note[x])
        media = float(media/len(note[x]))
        dict_medie[x] = media
        if media >= 5.0:
            print(x, '\t', studenti[x], '\t', media)
            cnt = cnt + 1
    if cnt == 0:
        print("Nu exista studenti promovati!")
    return dict_medie

def sortareMedie(studenti, note, medie):
    dictionary_items = medie.values()
    sorted_items = sorted(dictionary_items)
    for x in medie:
        print(studenti[x])



def infoAutor():
    print("\nProgramul a fost realizat de catre Tirla Petru!")

for x in meniu:
    print(meniu[x], end = '')

option = input("Enter your option: ")

dict_stud={}
dict_note={}
dict_medie={}
while option != '9':
    if option == '1':
        introduStudent(dict_stud, dict_note)
    elif option == '2':
        afisareStudenti(dict_stud)
    elif option == '3':
        afisareNote(dict_note)
    elif option == '4':
        afisareStudNote(dict_stud, dict_note)
    elif option == '5':
        cautareStudent(dict_stud, dict_note)
    elif option == '6':
        afisarePromovati(dict_stud, dict_note)
    elif option == '7':
        sortareMedie(dict_stud, dict_note, dict_medie)
    elif option == '8':
        infoAutor()
    else:
        print("Invalid option.")

    for x in meniu:
        print(meniu[x], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")

