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

def introduStudent(studenti, note):
    id = int(input("Introdu ID-ul studentului: "))
    nume = input("Numele studenului: ")
    Note = input("Introdu notele: ")
    Note = Note.split()
    note_vector = []
    for x in Note:
        note_vector.append(int(x))
    studenti[id] = nume
    note[id] = note_vector
    return studenti, note

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
    cautat = input("Introdu numele studentului cautat: ")
    for x in studenti:
        if studenti[x] == cautat:
            print("\nID\tNume student\tNote\n",
                  "___________________________________")
            print(x, '\t', studenti[x], end = '\t')
            for y in note[x]:
                print(y, end=' ')
            print()
        else:
            print("Studentul nu este in baza de date!")
    return False

def afisarePromovati(studenti, note):
    cnt = 0
    print("\nID\tNume student\tMedia\n",
          "___________________________________")
    for x in note:
        media = 0
        for y in note[x]:
            media = media + y
        media = float(media/len(note[x]))
        if media >= 5.0:
            print(x, '\t', studenti[x], '\t', media)
            cnt = cnt + 1
    if cnt == 0:
        print("Nu exista studenti promovati!")

def infoAutor():
    print("\nProgramul a fost realizat de catre Tirla Petru!")

for x in meniu:
    print(meniu[x], end = '')

option = input("Enter your option: ")

studenti = {}
note = {}

while option != '8':
    if option == '1':
        introduStudent(studenti, note)
    elif option == '2':
        afisareStudenti(studenti)
    elif option == '3':
        afisareNote(note)
    elif option == '4':
        afisareStudNote(studenti, note)
    elif option == '5':
        cautareStudent(studenti, note)
    elif option == '6':
        afisarePromovati(studenti, note)
    elif option == '7':
        infoAutor()
    else:
        print("Invalid option.")

    for x in meniu:
        print(meniu[x], end='')
    option = input("Enter your option: ")

print("\nThanks for using this program. Goodbye!")
