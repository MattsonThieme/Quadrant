import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

## Define size of the image, multiply by 255 to make the base image white
size = 500
data = np.ones((size,size), dtype=np.uint8)
data *= 255

## Set fraction of pixels to be blanked
frac = 0.65
num = int(size*size*frac)  # number of pixels to set to zero based on frac
pts = random.sample(range(size*size), num)

## Blank pixels defined in pts
## Basically, pts is a 1D array of values between 0 and the total number of pixels.
## To blank the pixels, I'm wrapping those values around. FYI: the int function runds down.
## For example: if size=50 and some value in pts is 104, we'll blank out the pixel in
## the third row [int(i/size)] and fourth column [i-size*int(i/size)]
for i in pts:
	data[int(i/size)][i-size*int(i/size)] = 0

## Set all pixels outside the circle to zero
for row in range(size):
	for col in range(size):
		if (np.sqrt(row**2 + col**2)) >= size:
			data[row][col] = 0

img = Image.fromarray(data, 'L')
img.show()
