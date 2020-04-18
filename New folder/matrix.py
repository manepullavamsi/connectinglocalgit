'''Given 2 matrices. One big matrix(say, A) and one small matrix(say, B). You need to find out whether the smaller one matrix is the sub-matrix(part) of bigger matrix.
Input:

Matrix A= 1   2   3   4

5   6   7   8

9  10 11 12

13 14 15 16




Matrix B = 6   7    8

10 11 12

14 15 16

Output: YES

 '''





r,c=map(int,input("enter no rows and columns :  ").split(" "))
m=[]#main matrix
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("enter a matrix values : ")))
    m.append(a)
print(m)
print("sub matrix")
sr,sc=map(int,input("enter a no columns and rows of submatrix :  ").split(" "))
s=[]#submatrix
for i in range(sr):
    a=[]
    for j in range(sc):
        a.append(int(input("enter a values of submatrix")))
    s.append(a)
print(s)
ms=[]
def sub(row,col):
    #possible submatrices of main matrix
    if r-1 == row and c-1 != col:
        A=[]
        for i in range(row):
            a=[]
            for j in range(1,col):
                a.append(m[i][j])
            A.append(a)
        ms.append(A)
    elif c-1 == col and r-1 != row:
        A=[]
        for i in range(1,row):
            a=[]
            for j in range(col):
                a.append(m[i][j])
            A.append(a)
        ms.append(A)
    elif c-1 == col and r-1 == row:
        A=[]
        for i in range(row):
            a=[]
            for j in range(col):
                a.append(m[i][j])
            A.append(a)
        ms.append(A)
    elif c == col and r == row:
        A=[]
        for i in range(1,row):
            a=[]
            for j in range(1,col):
                a.append(m[i][j])
            A.append(a)
        ms.append(A)

sub(r-1,c)
sub(r,c-1)
sub(r-1,c-1)
sub(r,c)
for i in ms:
    print("")
    print(i)
    print("")
if s in ms:
    print("True")
else:
    print("False")
        
        
        
