# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:38:34 2019

@author: Admin
"""

import numpy as np
def obj_func(x):
    a=x[0]
    b=x[1]
    A=0
    B=0
    for i in range(1,6):
        A+=i*np.cos((i+1)*a+i)
        B+=i*np.cos((i+1)*b+i)
    return A*B

def metropolis(x):
    global k,T_max
    return np.exp(-x/k*T_max)
        
T_max=25000 #Suitably high temperature as initial
T_min=2.5 #Suitably low min temperature as final
c=0.5 #reduction factor
n=300 #o. of iterations in each step
step_size=5 #we take a random but small stepsize
k=1
X=np.random.randint(1,255,size=2)
while T_max>T_min:
    print("Temperature:",T_max)
    for i in range(n):
        X1=X-np.array([step_size, step_size])+np.random.rand(2)*step_size*2 #generate new solution
        X1[0]=max(0,min(X1[0],255))
        X1[1]=max(0,min(X1[1],255)) #bringing values in range
        diff=obj_func(X1)-obj_func(X)
        if diff<=0:
            X=X1
        else:
            if np.random.rand()<=metropolis(diff):
                X=X1
    T_max=T_max*c
    print("Present solution: ",X)
    print("Present Fitness",obj_func(X))
print(60*"=")
print("Final solution:",X)
print("Final fitness:",obj_func(X))