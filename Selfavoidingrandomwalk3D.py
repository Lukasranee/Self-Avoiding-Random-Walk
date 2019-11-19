#Self Avoiding Random walk in 3 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def random_walk(n):
    #this function computes the SAW in 3 dimension
    x, y, z = 0, 0, 0
    dx,dy,dz = 0, 0, 0
    dxn, dyn, dzn = 0, 0, 0
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
    distancex.append(x)
    distancey.append(y)
    distancez.append(z)
    
    (dxn, dyn, dzn) = random.choice([(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)])
    while startstop == 0:           
        dx = dxn
        dy = dyn
        dz = dzn
        x += dxn
        y += dyn
        z += dzn
        if dx == 1:
            dxn,dyn,dzn = random.choice([(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])
        elif dx == -1:
            dxn,dyn,dzn = random.choice([(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])
        elif dy == 1:
            dxn,dyn,dzn = random.choice([(1,0,0),(-1,0,0),(0,1,0),(0,0,1),(0,0,-1)])
        elif dy == -1:
            dxn,dyn,dzn = random.choice([(1,0,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)])
        elif dz == 1:
            dxn,dyn,dzn = random.choice([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1)])
        elif dz == -1:
            dxn,dyn,dzn = random.choice([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1)])
        distancex.append(x)
        distancey.append(y)
        distancez.append(z)
        N += 1
        for seek in range(0,N):
            if x == distancex[seek] and y == distancey[seek] and z == distancez[seek]:
                startstop =1
                distancex.append(x)
                distancey.append(y)
                distancez.append(z)
        victory +=1
    endtoend = (x**2 + y**2 + z**2)**(1/2)
    endtoendsqrt = endtoend**2
    return distancex, distancey, distancez, endtoend, endtoendsqrt, S, pvec, N


kb = 1.38065 * (10**-23) #boltzman constant
entropyvec = [ ] # entropy
number_of_steps_vec = [ ]
stepvec = [ ]
stepvec1 = [ ]
number_of_walks = 10000
averagedistance = [ ]
averagedistancesqrt = [ ]
for walk_lengths in range(number_of_walks):    
        distance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        stepvec.append(distance[7])
        averagedistance.append(distance[3])
        averagedistancesqrt.append(distance[4])
avN = sum(stepvec)/len(stepvec)

number_of_walks = 300
for walk_lengths in range(10,number_of_walks):
    distance = random_walk(walk_lengths)
    stepvec1.append(walk_lengths)
    fraction = distance[7] / number_of_walks
    S = kb * math.log(fraction*(5 **(walk_lengths - 2))) / ((walk_lengths - 2) **2)
    entropyvec.append(S)



avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
p = np.log(avdissqrt)/np.log(avN)
v = p/2
#Flory mean field theory
d = 3
vf = 3 / (d+2)

print('steps: ',avN)
print('The average distance is: ',avdis)
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
ax.set_title('SAW in Three Dimensions')
plt.show()

entropyfig = plt.figure(2)
plt.plot(stepvec1,entropyvec)
plt.title('Entropy / Monomer for SAW in Three Dimensions')
plt.xlabel('Walks')
plt.ylabel('Entropy')
plt.show()