def introduDateFisier():
    nrLinii = 0
    sudoku = []

    with open('input.txt') as f:
        while nrLinii < 9:
            lin = f.readline()
            nrLinii += 1
            linie = [int(x) for x in lin.split(',')]
            sudoku.append(linie)

    return sudoku

def citesteMatrice(f):
    sudoku = [[0 for i in range(9)] for j in range(9)]

    n = int(f.readline())
    linii = f.readlines()
    for i in range(n):
        lin = linii[i].split()
        linie = int(lin[0])
        col = int(lin[1])
        nr = int(lin[2])
        sudoku[linie-1][col-1] = nr

    return sudoku
