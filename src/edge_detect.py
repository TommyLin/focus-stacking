#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters

image=mpimg.imread('../images/fly.jpg')

edges = filters.sobel(image)
plt.imshow(edges, cmap='gray')
plt.show()

mpimg.imsave('fly_edge.jpg', edges)
