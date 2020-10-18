# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:12:48 2020

@author: User
"""

def isPrime(x):
    if x==1 or x<=0:
        return False
    end=int(x**0.5)
    for i in range(2,end+1):
        if x%i==0:
            return False
    return True


def main():
    c=int(input("Enter the number:"))
    print("Is ",c," is Prime or Not? - ",isPrime(c))


main()
