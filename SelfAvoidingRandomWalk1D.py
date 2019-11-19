#Self Avoiding Random Walk in 1 dimensional space @Lukas Rane
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk(n):
    #this function computes the random walk in 1 dimension
    x = 0
    xdistance = [ ]
    xdistance.append(x)
    for i in range(n):
        dx = 0
        dx = random.choice([-1,1])
        if xdistance[-1] != dx:
            x += dx
            xdistance.append(x)
    return xdistance


kb = 1.38065 * (10**-23) #boltzman constant
entropyvec = [ ] # entropy
x = 0 #starts at the origin

number_of_steps_vec = [ ] #all different number of steps used
number_of_walks = 1000
number_of_steps_vec.append(0)

for walk_lengths in range(number_of_walks):    
        xdistance = random_walk(walk_lengths)
        number_of_steps_vec.append(walk_lengths)
        S = kb * math.log(2**(number_of_walks-2))/((number_of_walks -2) **2)
        entropyvec.append(S)


averagedistance = (abs(sum(xdistance))/len(xdistance))
print('The average distance is: ',averagedistance)

plt.figure(1)
plt.plot(xdistance)
plt.xlabel('Steps')
plt.ylabel('Distance')
plt.title('1-d random walk')
plt.show()    