# -*- coding: utf-8 -*-
#Self Avoiding Random Walk with Biased Sampling 2 dimensions @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import operator
from functools import reduce

def random_walk(n):
    #this function computes the SAW by biased sampling in 2 dimension
    x, y = 0, 0
    dx, dy = 0, 0
    dxn,dyn = 0,0
    
    kb = 1.38065 * (10**-23) #boltzman constant
    victory = 0
    averagebiased = 0
    startstop = 0
    distancex = [ ]
    distancey = [ ]
    availx = [ ]
    availy = [ ]
    avdistance = [ ]
    entropyvec = [ ]
    pvec = [ ]
    stepvec = [ ]
    avdisvec = [ ]
    denominatorvec = [ ]
    availperN = 0
    distancex.append(x)
    distancey.append(y)
    availx.append(x)
    availy.append(y)
    avec = [ ]
    N = 0
    while startstop == 0:
        
        N +=1
        
        direction = possibledirection(availx,availy,N,x,y)
        startstop = direction[2]
        dx,dy = 0,0
        if direction[1] != 0:
            availperN = direction[1]
        if direction[0] == 'right':
            (dx,dy) = (1,0)           
        elif direction[0] == 'left':
            (dx,dy) = (-1,0)
        elif direction[0] == 'up':
            (dx,dy) = (0,1)
        elif direction[0] == 'down':
            (dx,dy) = (0,-1)
        x += dx
        y += dy
        
        if startstop != 1:
            distancex.append(x)
            distancey.append(y)
            availx.append(x)
            availy.append(y)
        
        
        for seek in range(0,N):
            if x == distancex[seek] and y == distancey[seek]:
                startstop = 1
        
        avec.append(availperN)
    a = reduce(operator.mul, avec, 1)
    avdisbiased = (x**2 + y**2)*a
   
    endtoend = (x**2 + y**2)**0.5
    endtoendsqrt = endtoend**2
    nominator = endtoendsqrt*a
    avdistance.append(endtoend)
    
    return distancex, distancey, endtoend, endtoendsqrt, entropyvec, pvec, N, avdisbiased,a

def possibledirection(availx, availy, N, x, y):
    avail = ['right','left','up','down']
    availper = 0
    startstop = 0
    direction = 0
    for k in range(0,N):
        if availx[k] == x + 1 and availy[k] == y:
            avail.remove('right')
        if availx[k] == x - 1 and availy[k] == y:
            avail.remove('left')
        if availy[k] == y + 1 and availx[k] == x:
            avail.remove('up')
        if availy[k] == y - 1 and availx[k] == x:
            avail.remove('down')
    if len(avail) == 0:
        startstop = 1
    if len(avail) != 0:
        direction = random.choice(avail)
        availper = len(avail)
    return direction, availper, startstop



number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 1000
entropyvec = [ ]
stepvec = [ ]
stepvec1 = [ ]
averagedistance = [ ]
averagedistancesqrt = [ ]
biasedvec = []
averagebiased = 0
denominator = [ ]
for walk_lengths in range(number_of_steps):    
        distance = random_walk(walk_lengths)
        stepvec.append(distance[6])
        averagedistance.append(distance[2])
        averagedistancesqrt.append(distance[3])
        biasedvec.append(distance[7])
        denominator.append(distance[8])
averagebiased =((sum(biasedvec)/sum(denominator)))


avN = sum(stepvec)/len(stepvec)
avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)



p = np.log(avdissqrt)/np.log(avN)
v = p/2
#Flory mean field theory
d = 2
vf = 3 / (d+2)

print('The average distancessqrt is: ',avdissqrt)
print('The average distance is: ',avdis)
print('p value: ',p)
print('v: ',v)
print('flory mean field theory v: ',vf)
print('Average steps',avN)
print('N^2: ',avN**p)
print('Biased value: ',averagebiased)
plt.figure(1)
plt.plot(distance[0],distance[1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('SAW by Biased Sampling in TWO Dimensions')
plt.plot(0, 0, '*', label='starting point')
plt.plot(distance[0][-1], distance[1][-1], '*', label='end point')
plt.show()  

entropyfig = plt.figure(2)
plt.plot(distance[3])
plt.title('2D SAW Biased: Entropy / Monomer')
plt.xlabel('Walks')
plt.ylabel('Entropy')
plt.show()