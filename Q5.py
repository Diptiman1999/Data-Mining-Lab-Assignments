# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:30:41 2020

@author: User
"""
def check(arr):
    i=0
    flag=False
    while(i<len(arr)-1):
        if(arr[i]<=arr[i+1]):
            flag=True
        else:
            flag=False
            break
        i+=1
    if flag==True:
        return True
    else:
        i=0
        
        while(i<len(arr)-1):
            if(arr[i]>=arr[i+1]):
                flag=True
            else:
                flag=False
                break
            i+=1
    return flag
    
def main():
    n=int(input("Enter the size:"))
    arr=[]
    for i in range(0,n):
        arr.append(int(input("Enter the number:")))
    print("Is ",arr," is sorted ? - ",check(arr))
    
main()