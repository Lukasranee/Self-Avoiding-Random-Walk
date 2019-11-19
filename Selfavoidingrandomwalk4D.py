#Self Avoiding Random walk in 4 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import math

def random_walk(n):
    #this function computes the random walk in 1 dimension
    x, y, z, w = 0, 0, 0, 0
    startstop = 0
    victory = 0
    N = 0
    kb = 1.38065 * (10**-23)
    distancex = [ ]
    distancey = [ ]
    distancez = [ ]
    distancew = [ ]
    avdistance = [ ]
    avdistanceN = [ ]
    entropyvec = [ ]
    pvec = [ ]
    stepvec = [ ]
    S = 0
    distancex.append(x)
    distancey.append(y)
    distancez.append(z)
    distancew.append(w)
    (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
    while startstop == 0:
        dx = dxn
        dy = dyn
        dz = dzn
        dw = dwn
        x += dx
        y += dy
        z += dz
        w += dw
        if dx ==1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        elif dx == -1:
             (dxn, dyn, dzn, dwn) = random.choice([(-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        elif dy == 1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        elif dy == -1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        elif dz == 1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,0,1), (0,0,0,-1)])
        elif dz == -1:
            (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)])
        elif dw == 1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1)])
        elif dw == -1:
             (dxn, dyn, dzn, dwn) = random.choice([(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,-1)])
        distancex.append(x)
        distancey.append(y)
        distancez.append(z)
        distancew.append(w)
        N +=1
        for seek in range(0,N):
            if x == distancex[seek] and y == distancey[seek] and z == distancez[seek] and w == distancew[seek]:
                startstop = 1
                distancex.append(x)
                distancey.append(y)
                distancez.append(z)
                distancew.append(w)
        victory +=1
    endtoend = (x**2 + y**2 + z**2 + w**2)**0.5
    endtoendsqrt = endtoend**2
    return distancex, distancey, distancez, distancew, endtoend, endtoendsqrt, S, pvec, N


kb = 1.38065 * (10**-23) #boltzman constant


number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 10000
entropyvec = [ ]
stepvec = [ ]
stepvec1 = [ ]
averagedistance = [ ]
averagedistancesqrt = [ ]

for walk_lengths in range(number_of_steps):    
        distance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        stepvec.append(distance[8])
        averagedistance.append(distance[4])
        averagedistancesqrt.append(distance[5])
avN = sum(stepvec)/len(stepvec)
        
number_of_walks = 300
for walk_lengths in range(10,number_of_walks):
    distance = random_walk(walk_lengths)
    stepvec1.append(walk_lengths)
    fraction = distance[8]/number_of_walks
    S = kb *math.log(fraction*(3**(walk_lengths-2)))/((walk_lengths-2)**2)
    entropyvec.append(S)
        
avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)

p = np.log(avdissqrt)/np.log(avN)
v = p/2
#Flory mean field theory
d = 4
vf = 3/(d+2)



print('The average distance is: ',avdis)

print('Average steps',avN)
print('p value: ',p)
print('v: ',v)
print('Flory mean field theory v: ',vf)
print('N^2: ',avN**2)
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
plt.plot(stepvec1,entropyvec)
plt.title('4D RW: Entropy per monomer')
plt.xlabel('Walks')
plt.ylabel('Entropy')
plt.show()