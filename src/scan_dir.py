#!/usr/bin/env python3

# from skimage.measure import compare_ssim
import matplotlib.image as mpimg
import sys
from os import listdir
from os.path import isfile, join
from skimage.metrics import structural_similarity


print("len(sys.argv) =", len(sys.argv), sys.argv)

if (len(sys.argv) >= 2):
    target_dir = sys.argv[1]
else:
    target_dir = "../images/group/"


imagefiles = [f for f in listdir(target_dir) if isfile(join(target_dir, f))]

print(target_dir, imagefiles)

images = []

for i, file_name in enumerate(imagefiles):
    images.append(mpimg.imread(target_dir + file_name))

print("Image files = ", len(images))

if len(images) < 2:
    exit

for i in range(len(images)):
    for j in range(len(images)-1, i, -1):
        ssim = structural_similarity(images[i], images[j], multichannel=True)
        print("({i},{j})".format(i=i, j=j), end=" {0:2.4f}, ".format(ssim))
    print()
