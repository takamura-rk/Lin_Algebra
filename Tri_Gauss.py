def tri_gauss(A,b):
    n=len(A)

    for k in range (n):
        c=0
        for i in range (k,n+1):
            c+=A[i][k]/A[k][k]
            b[i]=b[i]-c*b[k]
            A[i][k]=0
            for j in range(k,n+1):
                A[i][j]=A[i][j]-c*A[k][j]
    return A, b
A=[[1,2,3],[5,2,1],[3,-1,1]]
b=[5,5,6]
(A1,b1)=tri_gauss(A,b)



