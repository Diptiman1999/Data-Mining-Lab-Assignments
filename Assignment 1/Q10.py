# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:46:44 2020

@author: DIPTIMAN
"""

n=int(input("Enter the number(greater than 2): "))
if n>=2:
    factor=2
    num=n
    while(num>1):
        if(num%factor==0):
            print(factor)
            num=num//factor
        else:
            factor+=1
        
    
else:
    print("The number entered is less than 2")
