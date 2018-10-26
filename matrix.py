#matrix
n=int(input("Enter number of rows here"))
m=int(input("Enter number of columns here"))
l2=[]
columnSum=0
for i in range(n):
    l=[]
    j=m
    while j>0:
        f=int(input("Enter Number here"))
        l.append(f)
        j-=1
    l2.append(l)
for i in l2:
    print(i)
x=0
for i in l2:
    x+=1
    print(max(i)," is max in row no.", x)
x=0
for i in l2:
    x+=1
    print(sum(i), " is the sum of numbers in row", x)
for i in l2:
    
    for j in range(len(l2)):
        columnSum=        
