# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:10:11 2020

@author: DIPTIMAN
"""

import math
s=int(input("Enter the side :"))
n=int(input("Enter the number of side :"))
area=(n*(s**2))/(4*math.tan(math.pi/n))
print("Area of the polygon ",area)