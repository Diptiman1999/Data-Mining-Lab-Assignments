# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:25:16 2020

@author: DIPTIMAN
"""

pos=input("Enter the pos: ")
print(pos)
a,b=pos[0],pos[1]

a=ord(a)-0
b=ord(b)-97
if b%2==0:
    if a%2==0:
        print("The box is white")
    else:
        print("The box is black")
else:
    if a%2==0:
        print("The box is black")
    else:
        print("The box is white")