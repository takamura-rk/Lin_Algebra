def trans_v1(A):
    A_1 = [row[:] for row in A]  
    n = len(A_1)                 
    m = len(A_1[0])              
    
    T = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            T[j][i] = A_1[i][j]  

    return T

def trans_v2(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


A = [[1, 2], [2, 1], [1, 2]]
B = trans_v1(A)
C=trans_v2(A)
print(B,C)


