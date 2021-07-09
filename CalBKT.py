solutie = 0
def knight_tour(n, board):
    print("Introdu pozitia de inceput pentru cal (linie si coloana):")
    y = int(input("Linie = "))
    x = int(input("Coloana = "))
    knight_tour_rezolvare(n , board, x - 1, y - 1, counter = 0)

def print_board(board):
    for i in board:
        for j in i:
            print(j, end = " ")
        print()
    print()

def knight_tour_rezolvare(n, board, x, y, counter):
    global solutie
    if counter == n * n:
        solutie = 1
        return True
    # daca iesim in afara labirintului sau am trecut deja prin
    # acea casuta, trebuie sa ne intoarcem
    if (x < 0) or (x >= n) or (y < 0) or (y >= n) or board[y][x] != -1:
        return False
    # backtracking
    board[y][x] = counter
    for x_move, y_move in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
        if knight_tour_rezolvare(n, board, x + x_move, y + y_move, counter + 1):
            return True
    board[y][x] = -1
    return False

def citire_tastatura(n, board):
    n = int(input('Introdu dimensiunea tablei de sah: '))
    board = [[-1 for i in range(n)] for j in range(n)]
    return n, board

def alege_optiune():
    global solutie
    n = 0
    board = []
    meniu = {}
    meniu[0] = "1. Citire dimensiune tabla"
    meniu[1] = "2. Rezolvare parcurgere tabla"
    meniu[2] = "3. Afisare"
    meniu[3] = "4. Informatii autor"
    meniu[4] = "5. Iesire program"
    for i in range(5):
        print(meniu[i])
    optiune = int(input("Alege optiunea: "))
    while(optiune != 5):
        if optiune == 1:
            n, board = citire_tastatura(n, board)
        elif optiune == 2:
            knight_tour(n, board)
        elif optiune == 3:
            if solutie == 1:
                print("\nSolutie:\n")
                print_board(board)
            else:
                print("\nNu exista solutie!\n")
        elif optiune == 4:
            print("Programul a fost creat de catre Tirla Petru.\n")
        else:
            print("Invalid option.\n")
        for i in range(5):
            print(meniu[i])
        optiune = int(input("Alege optiunea: "))
        print()

alege_optiune()