#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters


#files = ["../images/fly1.jpg", "../images/fly2.jpg"]
files = ["../images/fly1.jpg"]

fig = plt.figure()

for filename in files:
    print (filename)
    image = mpimg.imread(filename)
    fig.add_subplot(2, 2, 1)
    plt.imshow(image)

    edges = filters.sobel(image)
    fig.add_subplot(2, 2, 2)
    plt.imshow(edges)

    blured = filters.gaussian(image, sigma=1, multichannel=True)
    mpimg.imsave("result-01.jpg", blured)
    fig.add_subplot(2, 2, 3)
    plt.imshow(blured)

    edges = filters.sobel(blured)
    mpimg.imsave("result-02.jpg", edges)
    fig.add_subplot(2, 2, 4)
    plt.imshow(edges)

plt.show()
