#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters


#files = ['../images/fly1.jpg', '../images/fly2.jpg']
files = ['../images/fly1.jpg']

fig = plt.figure()

for filename in files:
    print (filename)
    image = mpimg.imread(filename)
    ax = fig.add_subplot(2, 2, 1)
    ax.set_title('Original')
    plt.imshow(image)

    edges = filters.sobel(image)
    ax = fig.add_subplot(2, 2, 2)
    ax.set_title('Edge(Orig)')
    plt.imshow(edges)

    blured = filters.gaussian(image, sigma=1, multichannel=True)
    mpimg.imsave('result-01.jpg', blured)
    ax = fig.add_subplot(2, 2, 3)
    ax.set_title('Blur(Orig)')
    plt.imshow(blured)

    edges = filters.sobel(blured)
    mpimg.imsave('result-02.jpg', edges)
    ax = fig.add_subplot(2, 2, 4)
    ax.set_title('Edge(Blured)')
    plt.imshow(edges)

plt.show()
