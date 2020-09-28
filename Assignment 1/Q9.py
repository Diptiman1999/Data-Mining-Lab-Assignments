# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:09:41 2020

@author: DIPTIMAN
"""

print(end="  ")
for i in range(1,11):
    print(i,end=" ")
print()
for i in range(1,11):
    print(i,end=" ")
    for j in range(1,11):
        mul=i*j
        print(i*j,end=" ")
    print()