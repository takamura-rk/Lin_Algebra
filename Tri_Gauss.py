def tri_gauss(A, b):
    n = len(A)
    # Copie pour ne pas modifier les originaux
    A = [row[:] for row in A]
    b = b[:]

    # Triangulation (élimination de Gauss)
    for k in range(n):
        for i in range(k+1, n):
            if A[k][k] == 0:
                raise ZeroDivisionError("Pivot nul, méthode échoue.")
            c = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= c * A[k][j]
            b[i] -= c * b[k]

    return A, b

A = [[1, 2, 3],
     [5, 2, 1],
     [3, -1, 1]]
b = [5, 5, 6]

A1, b1 = tri_gauss(A, b)
print(A1,b1)




