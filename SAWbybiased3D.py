# -*- coding: utf-8 -*-
#SAW by biased sampling with Biased Sampling in 3 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import operator
from functools import reduce

def random_walk(n):
    #this function computes the SAW in 3 dimensions
    x, y, z = 0, 0, 0
    startstop = 0
    N = 0
    victory = 0
    distancex = [ ]
    distancey = [ ]
    distancez = [ ]
    avdistance = [ ]
    entropyvec = [ ]
    pvec = [ ]
    stepvec = [ ]
    availx = [ ]
    availy = [ ]
    availz = [ ]
    avsqrtperN = [ ]
    nominatorN = [ ]
    biasedvalue = [ ]
    alistN = [ ]
    jada = [ ]
    a = 0
    availx.append(x)
    availy.append(y)
    availz.append(z)
    distancex.append(x)
    distancey.append(y)
    distancez.append(z)
    N = 0
    while startstop == 0:
        N += 1
        availperN = 1
        direction = possibledirection(availx,availy,availz,N,x,y,z)
        startstop = direction[2]
        dx,dy,dz = (0,0,0)
        if direction[0] == 'right':
            dx,dy,dz = (1,0,0)
        elif direction[0] == 'left':
            dx,dy,dz = (-1,0,0)
        elif direction[0] == 'up':
            dx,dy,dz = (0,1,0)
        elif direction[0] == 'down':
            dx,dy,dz = (0,-1,0)
        elif direction[0] == 'in':
            dx,dy,dz = (0,0,1)
        elif direction[0] == 'out':
            dx,dy,dz = (0,0,-1)
        x += dx
        y += dy
        z += dz
        distancex.append(x)
        distancey.append(y)
        distancez.append(z)
        availx.append(x)
        availy.append(y)
        availz.append(z)
        victory +=1
        jada.append(availperN)
    endtoend = (x**2 + y**2 + z**2)**(1/2)
    endtoendsqrt = endtoend**2
    
    return distancex, distancey, distancez, endtoend, endtoendsqrt, N


def possibledirection(availx, availy, availz, N, x, y, z):
    avail = ['right','left','up','down','in','out']
    availper = 1
    startstop = 0
    m = 0
    direction = 0
    for k in range(0,N):
        if availx[k] == x + 1 and availy[k] == y and availz[k] == z:
            avail.remove('right')
        if availx[k] == x - 1 and availy[k] == y and availz[k] == z:
            avail.remove('left')
        if availy[k] == y + 1 and availx[k] == x and availz[k] == z:
            avail.remove('up')
        if availy[k] == y - 1 and availx[k] == x and availz[k] == z:
            avail.remove('down')
        if availz[k] == z + 1 and availx[k] == x and availy[k] == y:
            avail.remove('in')
        if availz[k] == z - 1 and availx[k] == x and availy[k] == y:
            avail.remove('out')
    if len(avail) == 0:
        startstop = 1
    if len(avail) != 0:
        direction = random.choice(avail)
        availper = len(avail)
        m += 1
    return direction, availper, startstop, m



kb = 1.38065 * (10**-23) #boltzman constant
entropyvec = [ ] # entropy
x = 0 #starts at the origin

number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 10
entropyvec = [ ]
stepvec = [ ]
stepvec1 = [ ]
averagedistance = [ ]
averagedistancesqrt = [ ]
biasednum = [ ]
biaseddenominator = [ ]

for walk_lengths in range(number_of_steps):    
        distance = random_walk(walk_lengths)
        stepvec.append(distance[5])
        averagedistance.append(distance[3])
        averagedistancesqrt.append(distance[4])
        
avN = sum(stepvec)/len(stepvec)


avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)



p = np.log(avdissqrt)/np.log(avN)
v = p/2
#Flory mean field theory
d = 3
vf = 3 / (d+2)

print('Biasedvalue',biasedvalue)
print('steps: ',avN)
print('The average distance is: ',avdis)
print('Average square distance: ', avdissqrt)
print('p value: ',p)
print('v: ',v)
print('Flory mean field theory v: ',vf)
print('N^2: ',avN**p)
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[0], distance[1], distance[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('SAW by Biased Sampling in Three Dimensions')
plt.show()

#entropyfig = plt.figure(2)
#plt.plot(distance[4])
#plt.title('3D RW: Entropy per monomer')
#plt.xlabel('Steps')
#plt.ylabel('Entropy')
#plt.show()