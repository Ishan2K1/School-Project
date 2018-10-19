# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:13:59 2018

@author: Ishan Khandelwal
"""

#Bubble Sort
l1=[]
while True:
    m=input("Enter Number Here")
    if m!="":
        l1.append(int(m))
    else:
        break
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