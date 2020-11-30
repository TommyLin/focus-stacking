#!/usr/bin/env python3

import sys

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


if len(sys.argv) > 1:
    fig = plt.figure()
    no_images = len(sys.argv) - 1
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        image = mpimg.imread(sys.argv[i])
        fig.add_subplot(1, no_images, i)
        plt.imshow(image)
        if i != 1:
            plt.axis("off")
    plt.show()
