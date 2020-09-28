# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:37:06 2020

@author: DIPTIMAN
"""

n=int(input("Enter the number: "))
sum=0
num=0
while(n!=0):
    sum+=n
    num+=1
    n=int(input("Enter the number: "))
else:
    if num==0:
        print("Sorry nothing is been entered ")
    else:
        print("Average is ",sum/num)
    