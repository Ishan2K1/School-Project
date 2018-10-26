#matrix
#matrix
n=int(input("Enter number of rows here"))
m=int(input("Enter number of columns here"))
l2=[]
cSum=0
for i in range(n):
    l=[]
    j=m
    while j>0:
        f=int(input("Enter Number here"))
        l.append(f) 
        j-=1
    l2.append(l)
x=0 
for i in l2:
    print(l2[x],sum(i),max(i))
    x+=1
for j in range(n):
    for i in range(m):
        cSum+=l2[i][j]
    print(cSum, end="\t")
    cSum=0
dSum=0
f=0
for i in range(n):
    for j in range(m):
        while True:
