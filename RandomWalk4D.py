# -*- coding: utf-8 -*-
#Random walk in 4 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import math

def random_walk(n):
    #this function computes the random walk in 1 dimension
    x, y, z, w = 0, 0, 0, 0
    distancex = [ ]
    distancey = [ ]
    distancez = [ ]
    distancew = [ ]
    avdistance = [ ]
    distancex.append(x)
    distancey.append(y)
    distancez.append(z)
    distancew.append(w)
    endtoend = 0
    N = 1000
    for i in range(N):
        dx, dy, dz, dw = 0, 0, 0, 0
        (dx, dy, dz, dw) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        x += dx
        y += dy
        z += dz
        w += dw
        distancex.append(x)
        distancey.append(y)
        distancez.append(z)
        distancew.append(w)
    endtoend = (x**2 + y**2 + z**2 + w**2)**(1/2)
    endtoendsqrt = endtoend**2
    return distancex, distancey, distancez, distancew, endtoend, endtoendsqrt


kb = 1.38065 * (10**-23) #boltzman constant
entropyvec = [ ] # entropy
x = 0 #starts at the origin
averagedistance = [ ]
averagedistancesqrt = [ ]
number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 10000

for walk_lengths in range(number_of_steps):    
        distance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        S = kb * math.log(8**(number_of_steps-2))/((number_of_steps -2) **2)
        entropyvec.append(S)
        averagedistance.append(distance[4])
        averagedistancesqrt.append(distance[5])

avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
avdis = sum(averagedistance)/len(averagedistance)
print('The average distance is: ',avdis)
p = np.log(avdissqrt)/np.log(1000)
print('p value: ',p)
print('N^2: ',1000**p)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[0], distance[1], distance[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Free Random Walk in Three Dimensions')
plt.show()
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[0], distance[1], distance[3])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('w')
ax.set_title('Free Random Walk in Three Dimensions')
plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[0], distance[2], distance[3])
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('w')
ax.set_title('Free Random Walk in Three Dimensions')
plt.show()

fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
ax.plot(distance[1], distance[2], distance[3])
ax.set_xlabel('y')
ax.set_ylabel('z')
ax.set_zlabel('w')
ax.set_title('Free Random Walk in Three Dimensions')
plt.show()

entropyfig = plt.figure(5)
plt.plot(number_of_steps_vec,entropyvec)
plt.title('4D RW: Entropy per monomer')
plt.xlabel('Steps')
plt.ylabel('Entropy')
plt.show()