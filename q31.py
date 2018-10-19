# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
l1=[]
while True:
    m=input("Enter words here")
    if m!="":
        l1.append(m)
    else:
        break
l2,l3=[],[]
for i in l1:
    if i not in l3:
        l3.append(i)
    else:
        continue
for i in l3:
    a=l1.count(i)
    l2.append(a)
dic=dict(zip(l3,l2))
print(dic)