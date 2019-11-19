# -*- coding: utf-8 -*-
#Random walk in 3 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def random_walk(n):
    #this function computes the random walk in 1 dimension
    x, y, z = 0, 0, 0
    distancex = [ ]
    distancey = [ ]
    distancez = [ ]
    avdistance = [ ]
    distancex.append(x)
    distancey.append(y)
    distancez.append(z)
    entropyvec = [ ]
    stepvec = [ ]
    endtoend = 0
    N = 1000
    for i in range(N):
        dx, dy, dz = 0, 0, 0
        (dx, dy, dz) = random.choice([(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)])
        x += dx
        y += dy
        z += dz
        distancex.append(x)
        distancey.append(y)
        distancez.append(z)
        S = kb * math.log(6**(N-2))/((N -2) **2)
        entropyvec.append(S)
        stepvec.append(i)
    endtoend = (x**2 + y**2 + z**2)**(1/2)
    endtoendsqrt = endtoend**2
    return distancex, distancey, distancez, endtoend, endtoendsqrt,entropyvec,stepvec


kb = 1.38065 * (10**-23) #boltzman constant
x = 0 #starts at the origin
averagedistance = [ ]
averagedistancesqrt = [ ]
number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 10000

for walk_lengths in range(0,number_of_steps):    
    distance = random_walk(walk_lengths)
    number_of_steps_vec.append(walk_lengths)
    averagedistance.append(distance[3])
    averagedistancesqrt.append(distance[4])
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
avdis = sum(averagedistance)/len(averagedistance)
print('The average distance is: ',avdis)
p = np.log(avdissqrt)/np.log(1000)
print(p)
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[0], distance[1], distance[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Free Random Walk in Three Dimensions')
plt.show()

entropyfig = plt.figure(2)
plt.plot(distance[6],distance[5])
plt.title('Entropy / Monomer for FRW in Three Dimensions')
plt.xlabel('Steps')
plt.ylabel('Entropy')
plt.show()