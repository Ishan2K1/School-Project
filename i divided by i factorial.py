# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:39:42 2018

@author: Ishan Khandelwal
"""

n=int(input("Enter value of n here"))
g=1
f=1
for i in range(1,n+1):
    g*=i
    f+=(i/g)
print(f)    