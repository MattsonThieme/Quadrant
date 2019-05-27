import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

## Define size of the image, multiply by 255 to make the base image white
size = 500
data = np.ones((size,size), dtype=np.uint8)
data *= 255

## Set fraction of pixels to be blanked
frac = 0.40

num = int(size*size*frac)  # number of pixels to set to zero based on frac
x = random.sample(range(size*size), num)  # non-repeating random x points
y = random.sample(range(size*size), num)  # non-repeating random y points
pts = list(zip(x, y))

## Blank pixels defined in pts
## take i[0] modulo size as a single row/column could have multiple blanked pixels
for i in pts:
	data[i[0]%size][i[1]%size] = 0

## Set all pixels outside the circle to zero
for row in range(size):
	for col in range(size):
		if (np.sqrt(row**2 + col**2)) >= size:
			data[row][col] = 0

img = Image.fromarray(data, 'L')
img.show()
