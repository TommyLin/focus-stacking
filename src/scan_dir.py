#!/usr/bin/env python3

# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import matplotlib.image as mpimg

# import numpy as np
# import cv2
# import os
# import glob


# TODO Scan images files in directory automatically
target_dir = "../images/group/"


image1 = mpimg.imread(target_dir + "fly1.jpg")
image2 = mpimg.imread(target_dir + "fly2.jpg")
image3 = mpimg.imread(target_dir + "fly3.jpg")
image4 = mpimg.imread(target_dir + "fly4.jpg")

s12 = structural_similarity(image1, image2, multichannel=True)
s13 = structural_similarity(image1, image3, multichannel=True)
s14 = structural_similarity(image1, image4, multichannel=True)
s23 = structural_similarity(image2, image3, multichannel=True)
s24 = structural_similarity(image2, image4, multichannel=True)
s34 = structural_similarity(image3, image4, multichannel=True)


print("s1x {0:2.4f} {0:2.4f} {0:2.4f}".format(s12, s13, s14))
print("s2x          {0:2.4f} {0:2.4f}".format(s23, s24))
print("s3x                   {0:2.4f}".format(s34))
