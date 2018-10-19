# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:52:56 2018

@author: Ishan Khandelwal
"""
arr=[]
x=int(input("Enter no. of lists here"))
y=int(input("Enter no. of elements in each list here"))
b=0
for i in range(x):
    l1=[]
    for j in range(y):
        z=i*j
        l1.append(z)
        b+=1
    arr.append(l1)
    b=0
print(arr)