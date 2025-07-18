import numpy as np 
import math 
def det_mat(A,n):
    n=len(A)
    det=A[0][0]
    for i in range (n):
        det=det*A[i][i]



    return 