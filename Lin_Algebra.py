def sum_mat(A,B):
    a_1=len(A)
    a_0=len(A[0])
    b_1=len(B)
    b_0=len(B[0])

    C=[]
    if a_1==b_1 and a_0==b_0:
        for i in range (a_1):
            c=[]
            for j in range (a_0):
                c.append(A[i][j]+B[i][j])
            C.append(c)
        return C
    else:
        print("les matrices ne sont pas de même taille donc pas sommables")


A=[[1,2] ,[1,2],[2,1]]
B=[[3,3,2],[2,2,3]]


def mult_mat(A,B):
    a_1=len(A)
    a_0=len(A[0])
    b_1=len(B)
    b_0=len(B[0])

    C=[]
    
    if a_0==b_1:
        for i in range (a_1):
            c=[]
            for j in range (b_0):
                somme=0
                for k in range (a_0):
                   somme+= A[i][k]*B[k][j]
                c.append(somme)
            C.append(c)
        return C
    else :
        print (" les matrices ne peuvent pas être multiplier ")
