# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:05:08 2020

@author: User
"""

str1=input("Enter the first string:")
str2=input("Enter the second string:")
s=0
for x in str1:
   s+=ord(x)
for x in str2:
    s-=ord(x)
if(s==0):
    print(str1," is Anagram of ",str2)
else:
    print(str1," is not an Anagram of ",str2)
