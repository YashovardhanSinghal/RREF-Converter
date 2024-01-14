import numpy as np
import sympy as sym
f=open("testcase.txt")

row=int(f.readline())
col=int(f.readline())
li=[]
for line in f:
    m=[int(i) for i in line.split()]
    li.append(m)
f.close()
B=np.matrix(li)
l=sym.Matrix(B).rref()[0]
x = [l[i:i + col] for i in range(0, len(l), col)]
for i in x:
    for j in range(len(i)):
        i[j]=float(i[j])
        i[j]=round(i[j],5)
for i in x:
    for j in i:
        j=int(j)
pivot=[]
for i in range(row):
    for j in range(col):
        if x[i][j]==1:
            a=(i,j)
            break
    pivot.append(a)  
print("PIVOT POSITION:")     
print(pivot)
print("RREF:")
for i in x:
    for j in i:
        print(j,end=" ")
    print()
pivot_cols=[]
for i in x:
    for j in range(len(i)):
        if i[j]==1:
            pivot_cols.append(j)
freevaribale_cols=[]
for i in range(len(x[0])):
    if i not in pivot_cols:
        freevaribale_cols.append(i)
freevariable_colsvalues=[]
for j in freevaribale_cols:
    y=[]
    for i in x:
        y.append(i[j])
    freevariable_colsvalues.append(y)
for i in freevariable_colsvalues:
    for j in range(len(i)):
        i[j]=-i[j]
solutions=[]
for i in pivot_cols:
    k="x_"+str(i)
    solutions.append(k)
freevariables=[]
for i in freevaribale_cols:
    k="x_"+str(i)
    freevariables.append(k)
print("SOLUTION:")
for i in range(len(solutions)):
    a=f'{solutions[i]}='
    for j in range(len(freevariable_colsvalues)):
        a+=f'{freevariable_colsvalues[j][i]}*{freevariables[j]}'
    print(a)
for i in freevariables:
    print(f'{i} is a free variable')


    
        

