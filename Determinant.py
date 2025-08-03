def determinant(mat):
    n = len(mat)
    # Copie de la matrice 
    A = [row[:] for row in mat]
    det = 1
    swaps = 0

    for i in range(n):
        # Recherche d'un pivot non nul
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    swaps += 1
                    break
            else:
                return 0 
        pivot = A[i][i]
        for j in range(i + 1, n):
            factor = A[j][i] / pivot
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # Produit des éléments diagonaux
    for i in range(n):
        det *= A[i][i]
    return -det if swaps % 2 == 1 else det

matrice = [
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
]

print("Déterminant :", determinant(matrice))
