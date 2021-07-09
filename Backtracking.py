# Problema dispunerii reginelor

def regine_bkt(k):
    global n, x
    if k >= n:
        afisSolutie()
    else:
        for alfa in range(n):
            if posibil(k, alfa):
                x[k] = alfa
                regine_bkt(k+1)

def posibil(k, alfa):
    global x
    for i in range(k):
        if x[i] == alfa:
            return False
        if abs(x[i] - alfa) == k-i:
            return False
    else:
        return True

def afisSolutie():
    global n, x, nsol
    nsol += 1
    print("\nSolutia ", nsol, " x = ", x)
    for i in range(n):
        linie = ''
        for j in range(n):
            if x[j] == i:
                linie += 'R '
            else:
                linie += '. '
        print(linie)

n = 8
x = [0] * n
nsol = 0
regine_bkt(0)
if nsol == 0:
    print("Nu exista solutie")