#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


#image=mpimg.imread('../images/fly1.jpg')
if len(sys.argv) > 1:
    print (sys.argv[1])
    image=mpimg.imread(sys.argv[1])

plt.imshow(image)
plt.show()

