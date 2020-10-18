# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:01:22 2020

@author: User
"""

s=input("Enter the string:")
lower=0
upper=0
for x in s:
    if ord(x)>=65 and ord(x)<=90:
       upper+=1
    elif ord(x)>=97 and ord(x)<=122:
        lower+=1

print(s," has ",upper," uppercase and ",lower," lower case letters.")