# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:00:02 2018

@author: Ishan Khandelwal
"""
l1=[]
while True:
    m=input("enter numbers here")
    if m!="":
        l1.append(int(m))
    else:
        break
l1.sort()
x=int(input("Enter Number to Find here"))
while True:
    p=int(len(l1)/2)
    if x<l1[p-1]:
        l1=l1[0:p+1:1]
        if p==1:
            if p!=l1[0] and p!=l1[1]:
                print("not found")
                break
    elif x>l1[p]:
        l1=l1[p:len(l1)+1:1]
        if p==1:
            if p!=l1[0] and p!=l1[1]:
                print("not found")
                break
    elif p==1:
        if l1[0]==x:
            print("found")
            break
        elif l1[1]==x:
            print("found")
            break