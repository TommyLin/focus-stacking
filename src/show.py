#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


def images(filename):
    image=mpimg.imread(filename)
    plt.imshow(image)
    plt.show()

#image=mpimg.imread('../images/fly1.jpg')
if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        print (sys.argv[i])
        images (sys.argv[i])
