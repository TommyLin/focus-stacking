#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters

image=mpimg.imread('../images/fly1.jpg')

filtered_img = filters.gaussian(image, sigma=1, multichannel=True)

plt.imshow(filtered_img)
plt.show()

mpimg.imsave('fly1_blur1.jpg', filtered_img)
