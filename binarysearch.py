l1=[]
l2=[]
while True:
    m=input("enter numbers here")
    if m!="":
        l1.append(int(m))
    else:
        break
for i in range(len(l1)):
    l2.append(i)
dic=dict(zip(l1,l2))
l1.sort()
x=int(input("Enter Number to Find here"))
while True:
    p=round(len(l1)/2)
    if p==0:
        p=1
    if x<l1[p]:
        l1=l1[0:p]
        if p==1 or len(l1)==1:
            if x!=l1[0]:
                print("not found")
                break
    elif x>l1[p]:
        l1=l1[p:len(l1)]
        print(l1)
        if p==1 or len(l1)==1:
            if x!=l1[0]:
                print("not found")
                break
    elif p==1:
        if l1[0]==x:
            print("found",dic.get(x), "th position")
            break
        elif l1[1]==x:
            print("found",dic.get(x),"th position")
            break
    elif x==l1[p]:
        print("found",dic.get(x), "th position")
        break