#Bubble Sort
l1=eval(input("Enter list here"))
count=0
for i in range(len(l1)):
    for j in range(len(l1)-i-1):
        if l1[j]<=l1[j+1]:
            count+=1
            continue
        elif l1[j]>l1[j+1]:
            l1[j], l1[j+1]=l1[j+1], l1[j]
            count+=1
print(l1, "operations took place", count,"number of times")
