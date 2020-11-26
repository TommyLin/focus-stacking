#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters


#files = ['../images/fly1.jpg', '../images/fly2.jpg']
files = ['../images/fly1.jpg']

def get_gray(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def rgb2gray(image):
    gray = [[0 for i in range(image.shape[0])] for j in range(image.shape[1])]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gray[i][j] = get_gray(image[i][j])
    return gray

fig = plt.figure()

for filename in files:
    print (filename)
    image = mpimg.imread(filename)
    ax = fig.add_subplot(2, 2, 1)
    ax.set_title('Original')
    plt.axis('off')
    plt.imshow(image)

    edges = filters.sobel(image)
    ax = fig.add_subplot(2, 2, 2)
    ax.set_title('Edge(Orig)')
    plt.axis('off')
    plt.imshow(rgb2gray(edges))

    blured = filters.gaussian(image, sigma=1, multichannel=True)
    mpimg.imsave('result-01.jpg', blured)
    ax = fig.add_subplot(2, 2, 3)
    ax.set_title('Blur(Orig)')
    plt.imshow(blured)

    edges = filters.sobel(blured)
    mpimg.imsave('result-02.jpg', edges)
    ax = fig.add_subplot(2, 2, 4)
    ax.set_title('Edge(Blured)')
    plt.axis('off')
    plt.imshow(rgb2gray(edges))

plt.show()
