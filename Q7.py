# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:47:34 2020

@author: User
"""

l=[]
x=input("Enter the string:")
while x!="":
    if x not in l:
        l.append(x)
    x=input("Enter the string:")
else:
    for i in l:
        print(i)