# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:16:29 2020

@author: User
"""

n=int(input("Enter the size:"))
s=set()
for i in range(0,n):
    s.add(int(input("Enter the number:")))

print("Elements are ",s)
print("Maximum is ",max(s))
print("Minimum is ",min(s))