#!/usr/bin/env python3

import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
from skimage import filters


def gaussian_blur(fin="../images/fly1.jpg", fout="fly1_blur.jpg"):
    if fin == "" or fout == "":
        raise SyntaxError("No parameter")

    image = mpimg.imread(fin)
    blured = filters.gaussian(image, sigma=1, multichannel=True)
    mpimg.imsave(fout, blured)
