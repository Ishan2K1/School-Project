d={"rose":["pink","black","red"],"tulip":["pink","orange"],"poppy":["red"],"lily":["white","violet"]}
d2={}
for i in d:
    l=d.get(i)
    d2[i]=len(l)
print(d2)
d3={}
l2,l3=[]
for i in d:
    l=d.get(i)
    for j in l:
        l2.append(j)
for i in l2:
    l3.append(l2.count(i))
Max=max(l3)
for i in l2:
    if l2.count(i)==Max:
        print(i)
