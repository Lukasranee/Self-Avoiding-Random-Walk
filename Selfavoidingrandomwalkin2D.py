# -*- coding: utf-8 -*-
#Self Avoiding Random Walk 2 dimensions @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk(n):
    #this function computes the self avoiding random walk in 2 dimension
    x, y = 0, 0
    dx, dy = 0, 0
    dxn,dyn = 0,0
    N = 0
    victory = 0
    startstop = 0
    distancex = [ ]
    distancey = [ ]
    avdistance = [ ]
    entropyvec = [ ]
    pvec = [ ]
    stepvec = [ ]
    distancex.append(x)
    distancey.append(y)
    S = 0
    (dxn, dyn) = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
    while startstop == 0:
        dx = dxn
        dy = dyn
        x += dxn
        y += dyn
        if dx == 1:
            (dxn,dyn) = random.choice([(1,0),(0,1),(0,-1)])            
        elif dx == -1:
            (dxn,dyn) = random.choice([(-1,0),(0,1),(0,-1)])
        elif dy == 1:
            (dxn,dyn) = random.choice([(1,0),(-1,0),(0,1)])
        elif dy == -1:
            (dxn,dyn) = random.choice([(1,0),(-1,0),(0,-1)])
        distancex.append(x)
        distancey.append(y)
        N +=1
        for seek in range(0,N):
            if x == distancex[seek] and y == distancey[seek]:
                startstop = 1
                distancex.append(x)
                distancey.append(y)
        victory += 1
    endtoend = (x**2 + y**2)**0.5
    endtoendsqrt = endtoend**2
    return distancex, distancey, endtoend, endtoendsqrt, S, pvec, N



kb = 1.38065 * (10**-23) #boltzman constant
number_of_steps_vec = [ ] #all different number of steps used
number_of_walks = 10000
entropyvec = [ ]
stepvec = [ ]
stepvec1 = [ ]
averagedistance = [ ]
averagedistancesqrt = [ ]

for walk_lengths in range(2,number_of_walks):    
        distance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        stepvec.append(distance[6])
        averagedistance.append(distance[2])
        averagedistancesqrt.append(distance[3])
avN = sum(stepvec)/len(stepvec)     
        

number_of_walks = 300
for walk_lengths in range(10,number_of_walks):    
        distance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        stepvec1.append(walk_lengths)
        fraction = distance[6] / number_of_walks
        S = kb * math.log(fraction *(3 ** (walk_lengths - 2))) / ((walk_lengths - 2) ** 2)
        entropyvec.append(S)
        
avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
p = np.log(avdissqrt)/np.log(avN)
v = p/2
#Flory mean field theory
d = 2
vf = 3 / (d+2)

#averagestep


print('The average distance is: ', avdis)
print('p value: ',p)
print('v: ',v)
print('flory mean field theory v: ',vf)
print('Average steps',avN)
print('N^2: ',avN**p)
plt.figure(1)
plt.plot(distance[0],distance[1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('SAW in Two Dimensions')
plt.plot(0, 0, '*', label='starting point')
plt.plot(distance[0][-1], distance[1][-1], '*', label='end point')
plt.show()  

entropyfig = plt.figure(2)
plt.plot(stepvec1,entropyvec)
plt.title('Entropy / Monomer for SAW in Two Dimensions')
plt.xlabel('Walks')
plt.ylabel('Entropy')
plt.show()