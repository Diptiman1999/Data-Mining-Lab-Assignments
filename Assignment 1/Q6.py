# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:30:17 2020

@author: DIPTIMAN
"""

n=int(input("Enter the side :"))
if(n>=3 and n<=10 ):
    if(n==3):
        print("Triangle")
    elif(n==4):
        print("Quadrilateral")
    elif(n==5):
        print("Pentagon")
    elif(n==6):
        print("Hexagon")
    elif(n==7):
        print("Heptagon")
    elif(n==8):
        print("Octagon")
    elif(n==9):
        print("Nonagon")
    else:
        print("Decagon")
    
else:
    print("Wrong number of sides")