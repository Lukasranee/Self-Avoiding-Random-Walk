#Random walk in 1 D space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk():
    #this function computes the random walk in 1 dimension
    x = 0
    xdistance = [ ]
    averagedistance = [ ]
    xdistance.append(x)
    entropyvec = [ ]
    stepvec = [ ]
    N = 1000
    for i in range(N):
        dx = 0
        dx = random.choice([-1,1])
        x += dx
        xdistance.append(x)
        S = kb * math.log(2**(1000-2))/((1000 -2) **2)
        entropyvec.append(S)
        stepvec.append(i)
    endtoend = (x**2)**0.5
    endtoendsqrt = endtoend**2
    
    return xdistance, endtoend, endtoendsqrt, entropyvec,stepvec


kb = 1.38065 * (10**-23) #boltzman constant
entropyvec = [ ] # entropy
x = 0 #starts at the origin

xvec = [ ] #all different number of steps used
number_of_walks = 10000
averagedistancesqrt = [ ]
averagedistance = [ ]
number_of_steps_vec = [ ]

for walk_lengths in range(number_of_walks):    
        distance = random_walk()
        number_of_steps_vec.append(walk_lengths)
        averagedistancesqrt.append(distance[2])
        averagedistance.append(distance[1])
avdist = sum(averagedistance)/len(averagedistance)
avdistsqrt = sum(averagedistancesqrt)/len(averagedistancesqrt)
print('The average distance is: ',avdist)
p = np.log(avdistsqrt)/np.log(1000)
print('P value: ',p)
print('N^p: ', 1000**p)
fig = plt.figure(1)
plt.plot(distance[0])
plt.xlabel('Steps')
plt.ylabel('Distance')
plt.title('Free Random Walk in One Dimension')
plt.show()     

entropyfig = plt.figure(2)
plt.plot(distance[4],distance[3])
plt.title('Entropy / Monomer for FRW in One Dimension')
plt.xlabel('Steps')
plt.ylabel('Entropy')
plt.show()
