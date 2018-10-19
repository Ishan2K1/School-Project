#Insertion Sort
l1=[]
while True:
    m=input("Enter Number here")
    if m!="":
        l1.append(int(m))
    else:
        break
count=0
for i in range(1,len(l1)):
    key=l1[i]
    j=i-1
    while j>=0 and key<l1[j]:
        l1[j+1]=l1[j]
        j-=1
        count+=1
    l1[j+1]=key
        
print(l1, count)
