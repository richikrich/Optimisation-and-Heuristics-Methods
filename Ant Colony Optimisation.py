# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:02:52 2019

@author: Richik
"""
import numpy as np
import random

cities =np.array([[0.0333692,0.9925079],
                  [0.6020896,0.0168807],
                  [0.1532083,0.7020444],
                  [0.3181124,0.1469288],
                  [0.1878440,0.8679120],
                  [0.9786112,0.4925364],
                  [0.7918010,0.7943144],
                  [0.5145329,0.0363478],
                  [0.5500754,0.8324617],
                  [0.3893757,0.6635483],
                  [0.9641841,0.6400201],
                  [0.7718126,0.5463923],
                  [0.7549037,0.4584584],
                  [0.2837881,0.7733415],
                  [0.3308411,0.1974851],
                  [0.7977221,0.1193149],
                  [0.3221207,0.7930478],
                  [0.9201035,0.1186234],
                  [0.2397964,0.1448552],
                  [0.3967470,0.6716172]])
distance=np.zeros((20,20))
taboo=np.ones((20,20))
cumProb=np.zeros(20)
nextProb=np.zeros(20)

pheromoneLaid=5
evapRate=0.1
tau_ij=np.ones((20,20))
alpha=1
beta=1
bestDist=1000
bestRoute=np.zeros(20)

for i in range(len(distance)-1):
    for j in range(i+1,len(distance)):
        distance[i][j]=np.sqrt(np.square(cities[i][1]-cities[j][1])+np.square(cities[i][0]-cities[j][0]))
        distance[j][i]=distance[i][j]

for i in range(len(taboo)):
    taboo[i][i]=0

def updatePheromone(Visited,t_ij):
    sumDist=0
    global bestDist, bestRoute, distance, evapRate, pheromoneLaid
    for i in range(len(Visited)-1):
        x=int(Visited[i])
        y=int(Visited[i+1])
        sumDist=sumDist+distance[x][y]
    #sumDist=sumDist+distance[y][x]
    sumDist=sumDist+distance[y][x]
    if bestDist>sumDist:
        bestDist=sumDist
        bestRoute=Visited
    if sumDist == 0:
        print("Distance 0 in pheromone update")
        return
    for i in range(len(t_ij)):
        for j in range(len(t_ij)):
            if i!=j:
                t_ij[i][j]=(1-evapRate)*t_ij[i][j]
        t_ij[i][i]=0
    for i in range(len(Visited)-1):
        x=int(Visited[i])
        y=int(Visited[i+1])
        t_ij[x][y]=t_ij[x][y]+pheromoneLaid/sumDist
    t_ij[y][x]=t_ij[y][x]+pheromoneLaid/sumDist
    return t_ij
def updateTaboo(t_mat,p_node):
    for i in range(len(t_mat)):
        t_mat[i][p_node]=0
    return t_mat
def nextNodeProb(t_ij,t_mat,p_node):
    global distance, alpha, beta
    sumDen=0
    n_Prob=np.zeros(20)
    for j in range(len(n_Prob)):
        if t_mat[p_node][j]==0:
            n_Prob[j]=0
        else:
            sumDen=sumDen+(((t_ij[p_node][j])**alpha)/((distance[p_node][j]))**beta)
    for j in range(len(n_Prob)):
        if t_mat[p_node][j]==1:
            n_Prob[j]=(((t_ij[p_node][j])**alpha)/((distance[p_node][j]))**beta)/sumDen
    return n_Prob

for itrr in range(100):
    present_node=random.randint(0,19)
    print("present {}".format(present_node))
    Visited=np.zeros(20)
    for k in range(len(distance)):
        nextProb=nextNodeProb(tau_ij,taboo,present_node)
        nextNodeProbab=random.random()
        cumProb[0]=nextProb[0]
        nextNodeToGo=1
        if nextNodeProbab<cumProb[0]:
            nextNodeToGo=1
        for i in range(1,20):
            cumProb[i]=cumProb[i-1]+nextProb[i]
            if nextNodeProbab>cumProb[i-1] and nextNodeProbab<cumProb[i]:
                nextNodeToGo=i
        present_node=nextNodeToGo
        taboo=updateTaboo(taboo,present_node)
        Visited[k]=present_node
    print(itrr)
    tau_ij=updatePheromone(Visited,tau_ij)
    taboo=np.ones((20,20))
    for i in range(len(taboo)):
        taboo[i][i]=0
    print("Best Route so far {}".format(bestRoute))
    print("Best Distance so far {}".format(bestDist))
print("Best Final Route and Distance are {} and {}".format(bestRoute,bestDist))