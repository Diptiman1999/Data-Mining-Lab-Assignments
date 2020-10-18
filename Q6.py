# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:42:36 2020

@author: User
"""

l=[]
x=int(input("Enter the number:"))
while x!=0:
    l.append(x)
    x=int(input("Enter the number:"))
else:
    l.sort()
    for i in l:
        print(i)