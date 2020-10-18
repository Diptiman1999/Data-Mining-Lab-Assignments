# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:50:24 2020

@author: User
"""

s=input("Enter the string:")
sen=set()
for x in s:
    sen.add(x)
print("No of unique characters are ",len(sen))