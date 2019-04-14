import numpy as np
    
def objective_func(x):
    y=1-np.power(x,2)-2*x
    return y

def update_vel(x,C1,C2,localBestPosition,GlobalBestPosition,currentPosition):
    x=w*x+C1*np.random.random(1)[0]*(localBestPosition-currentPosition)+C2*np.random.random(1)[0]*(GlobalBestPosition-currentPosition)
    return x
    
def update_pos(x,currentVelocity):
    x+=currentVelocity
    return x

#control parameters
w=0.70
#acceleration constants
C1=0.20
C2=0.60
#size of swarm
sizeOfSwarm=10;

currentPosition=np.random.random(size=sizeOfSwarm)*10 - 5
currentVelocity=np.random.random(size=sizeOfSwarm)
GlobalBestFitness=0
GlobalBestPosition=0
currentFitness=objective_func(currentPosition)
localBestPosition=currentPosition.copy()
localBestFitness=currentFitness.copy()
for j in range(10):
    for i in range(sizeOfSwarm):
        if currentFitness[i]>=localBestFitness[i]:
            localBestFitness[i]=currentFitness[i]
            localBestPosition[i]=currentPosition[i]
            if localBestFitness[i]>GlobalBestFitness:
                GlobalBestFitness=localBestFitness[i]
                GlobalBestPosition=localBestPosition[i]
    print("Iteration:",j,"\n","\nLocal Best Positions: \n",localBestPosition,"\nLocal Best Fitness: \n",localBestFitness)
    currentVelocity=update_vel(currentVelocity,C1,C2,localBestPosition,GlobalBestPosition,currentPosition)
    currentPosition=update_pos(currentPosition,currentVelocity)

#approximately GBP=-1,GBF=-2            
print("Global Best Position: \n",GlobalBestPosition,"\nGlobal Best Fitness: \n",GlobalBestFitness)