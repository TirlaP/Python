board = [
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]
poz_init_x = 1
poz_init_y = 1
poz_finala_x = 3
poz_finala_y = 3

n = 5
m = 8

directii = 4
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def citire():
    pass

def isOK(i, j):
    global n, m, board, poz_finala_x, poz_finala_y

    if i > n or i < 0:
        return False
    if j > m or j < 0:
        return False

    if board[i][j] == 1 or (i == poz_finala_x and j == poz_finala_y):
        return True

    if board[i][j] == 0 or board[i][j]:
        return False

def afisare(board, n, m):

    for i in range(n):
        for j in range(m):
            print(board[i][j], end=" ")
        print()
    print()

def rezolvare(i, j, pas):
    global n, m, poz_finala_x, poz_finala_y, di, dj, board, directii

    if i == poz_finala_x and j == poz_finala_y:
        afisare(board, n, m)
    else:
        for k in range(directii):
            i_vecin = i + di[k]
            j_vecin = j + dj[k]
            if isOK(i_vecin, j_vecin):
                board[i_vecin][j_vecin] = pas
                rezolvare(i_vecin, j_vecin, pas + 1)
                board[i_vecin][j_vecin] = 0


print(rezolvare(poz_init_x, poz_init_y, 2))

