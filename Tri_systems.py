def solinf(L,b):
    n=len(L)
    X = [0] * n 
    for i in range(n):
        somme = 0
        for j in range(i):
            somme += L[i][j] * X[j]
        X[i] = (b[i] - somme) / L[i][i]
    return X

A=[[1,0,0],[2,3,0],[1,4,-1]]
b=[1,8,10]
x=solinf(A,b)
print(x)


def solsup(U,c):
    n=len(U)
    y=[0]*n
    for i in range(n - 1, -1, -1): 
        somme = 0
        for j in range(i + 1, n):
            somme+=U[i][j]*y[j]
        y[i]=(c[i]-somme)/U[i][i]
    return y
C=[[1,2,3],[0,4,8],[0,0,5]]
d=[6,16,15]
y=solsup(C,d)
print(y)