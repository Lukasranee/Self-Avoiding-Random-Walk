#Random Walk 2 dimensions @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk(n):
    #this function computes the random walk in 1 dimension
    x, y = 0, 0
    distancex = [ ]
    distancey = [ ]
    avdistance = [ ]
    dis = 0
    distancex.append(x)
    distancey.append(y)
    stepvec = [ ]
    entropyvec = [ ]
    endtoend = 0
    N = 1000
    for i in range(N):
        dx, dy = 0, 0
        (dx, dy) = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        x += dx
        y += dy
        distancex.append(x)
        distancey.append(y)
        S = kb * math.log(4**(N-2))/((N -2) **2)
        entropyvec.append(S)
        stepvec.append(i)
    
    endtoend = (x**2 + y**2)**0.5
    endtoendsqrt = endtoend**(2)
    return distancex, distancey, avdistance, endtoend, endtoendsqrt, entropyvec,stepvec


kb = 1.38065 * (10**-23) #boltzman constant
# entropy
x = 0 #starts at the origin

number_of_steps_vec = [ ] #all different number of steps used
number_of_steps = 10000
averagedistance = [ ]
averagedistancesqrt = [ ]
for walk_lengths in range(number_of_steps):    
    distance = random_walk(walk_lengths)
    number_of_steps_vec.append(walk_lengths)
    averagedistance.append(distance[3])
    averagedistancesqrt.append(distance[4])

avdis = sum(averagedistance)/len(averagedistance)
avdissqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
print('The average distance is: ',avdis)
p = np.log(avdissqrt)/np.log(1000)
print('p value: ',p)

stravdis = str(avdis)
strp = str(p)
print('N^2: ',number_of_steps**p)
plt.figure(1)
plt.plot(distance[0],distance[1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Free Random Walk in Two Dimension')
#text = 'Averagedistance: ' + stravdis, 'p value: ' + strp
#plt.text(min(distance[0]), max(distance[1]), text)
plt.show()  

entropyfig = plt.figure(2)
plt.plot(distance[6],distance[5])
plt.title('Entropy / Monomer for FRW in Two Dimension')
plt.xlabel('Steps')
plt.ylabel('Entropy')
plt.show()