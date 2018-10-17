# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:24:40 2018

@author: Ishan Khandelwal
"""
l1=[]
l2=[
while True:
    a=input("Enter Number Here")
    if a=="":
        break
    else:
        l1.append(int(a))
print(l1)
for i in l1:
    if i not in l2:
        l2.append(i)
        print("*"*l1.count(i))
