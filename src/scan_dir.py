#!/usr/bin/env python3

#from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import matplotlib.image as mpimg

#import numpy as np
#import cv2
#import os
#import glob


# TODO Scan images files in directory automatically
target_dir = "../images/group/"


image1 = mpimg.imread(target_dir + "fly1.jpg")
image2 = mpimg.imread(target_dir + "fly2.jpg")
image3 = mpimg.imread(target_dir + "fly3.jpg")

s12 = structural_similarity(image1, image2, multichannel=True)
s23 = structural_similarity(image2, image3, multichannel=True)
s13 = structural_similarity(image1, image3, multichannel=True)


print("s12={0:2.4f}".format(s12))
print("s23={0:2.4f}".format(s23))
print("s13={0:2.4f}".format(s13))

