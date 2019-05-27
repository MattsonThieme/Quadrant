import numpy as np
import matplotlib.pyplot as plt
import random

## Generate random distributions, zip them together
rng = 5000
x = [random.uniform(0,1) for i in range(rng)]
y = [random.uniform(0,1) for i in range(rng)]
z = list(zip(x,y))

## Check if each point is within the circle
z = [i for i in z if (np.sqrt(i[0]**2 + i[1]**2)) < 1]

## Split new zipped list back into lists we can plot
x = [i[0] for i in z]
y = [i[1] for i in z]

## Plotting
limits = 1
plt.scatter(x,y)
plt.axis('equal')  # Keeps the plot a square - kindof works
plt.xlim(0,limits)
plt.ylim(0,limits)

plt.show()