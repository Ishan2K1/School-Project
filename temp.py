# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s1=input("Enter any sentence here")
s2=input("Enter Any String here")
isEqual=""
b=""
word=""
current=""
s4=s1
s3=s1.lower()
s3=s3.lstrip()
s3=s3.rstrip()
l=s3.count(s3[1])
print(l)
print(s3)
if s1==s2:
    isEqual=s1
if s1.lower()==s2.lower():
    isEqual=s1
if s1.startswith("AAA"):
    b=s1
if isEqual=="" and b=="":
    print("The code does not support the entered text")
else:
    print(isEqual,b)
for i in s4:
    if i==" ":
        word=""
    else:
        word+=i
    if len(word)>len(current):
        current=word
print(current)