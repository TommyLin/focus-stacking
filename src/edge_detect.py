#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters

image=mpimg.imread(sys.argv[1])

edges = filters.sobel(image)
plt.imshow(edges, cmap='gray')
plt.show()

mpimg.imsave(sys.argv[2], edges)
