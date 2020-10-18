# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:20:11 2020

@author: User
"""

m=['January','February','March','April','May','June','July','August','September','October','November','December']
def magicdate(month,date,lasty):
    i=m.index(month)+1
    check=i*date
    return check==lasty
    
    
s=input("Enter the date:")
sn=s.split(",")
month=sn[0]
date=int(sn[1])
lasty=int(sn[2])%100
print("Is ",s," is a magic year -",magicdate(month,date,lasty))
        