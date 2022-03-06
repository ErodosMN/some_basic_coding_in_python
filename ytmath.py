# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:22:03 2019

@author: Megi, Mino, Jacob
"""

def row_insert(T1,x):
    
    if not T1:
        T1.append([x])
       
    else:
        for i in range (len(T1)-1,-1,-1):
            
            if x>=max(T1[i]):
                T1[i].append(x)
                return T1
            
            for j in range(len(T1[i])):
                if T1[i][j]>x:
                    x,T1[i][j]=T1[i][j],x
                    break
            
        T1.insert(0,[x])
        
    return T1

def mult_young(T1,T2):
    if T2!=[]:
        for row in T2:
            for x in row:
                assert type(x)==int
                T1=row_insert(T1,x)
    return T1
    