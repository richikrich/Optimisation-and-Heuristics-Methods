# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:35:49 2019

@author: Admin
"""

import random
import numpy as np

def objective_func(x):
    y=0
    z=0
    for i in range(1,6):
        y+=i*np.cos((i+1)*x[0]+i);
        z+=i*np.cos((i+1)*x[1]+i);
    t=y*z
    return t

#control parameters
w=0.7
#acceleration constants
c1=0.2
c2=0.6
#size of swarm
sizeOfSwarm=10

currentPosition=[]
currentVelocity=[]
currentFitness=[]
GlobalBestFitness=0
GlobalBestPosition=0
for i in range(0,sizeOfSwarm):
    currentPosition.append(np.array([random.randint(1,255),random.randint(1,255)]))
    currentVelocity.append(np.array([random.uniform(0,1),random.uniform(0,1)]))
    currentFitness.append(objective_func(currentPosition[i]))
    if(currentFitness[i]<GlobalBestFitness):
        GlobalBestFitness=currentFitness[i]
        GlobalBestPosition=currentPosition[i]
localBestPosition=currentPosition.copy()
localBestFitness=currentFitness.copy()
print("Initial Local Best Position: \n",localBestPosition)
print("Initial Local Best Fitness: \n",localBestFitness)
for j in range(100):
    for i in range(0,sizeOfSwarm):
        currentFitness[i]=objective_func(currentPosition[i])
        if(currentFitness[i]<localBestFitness[i]):
            localBestPosition[i]=currentPosition[i]
            localBestFitness[i]=currentFitness[i]
        if(localBestFitness[i]<GlobalBestFitness):
            GlobalBestFitness=localBestFitness[i]
            GlobalBestPosition=localBestPosition[i]
        (currentVelocity[i])[0]=w*((currentVelocity[i])[0])+c1*random.uniform(0,1)*((localBestPosition[i])[0]-(currentPosition[i])[0])+c2*random.uniform(0,1)*(GlobalBestPosition[0]-(currentPosition[i])[0])
        (currentVelocity[i])[1]=w*((currentVelocity[i])[1])+c1*random.uniform(0,1)*((localBestPosition[i])[1]-(currentPosition[i])[1])+c2*random.uniform(0,1)*(GlobalBestPosition[1]-(currentPosition[i])[1])
        currentPosition[i]=currentPosition[i]+currentVelocity[i]
    print("Iteration:",j)
    print("Local Best Position: \n",localBestPosition,"\nLocal Best Fitness: \n",localBestFitness)
print("Global Best Position:\n",GlobalBestPosition,"\nGlobal Best Fitness:\n",GlobalBestFitness)