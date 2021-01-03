#!/usr/bin/env python3

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys
from os import listdir
from os.path import isfile, join
from skimage import filters
from PIL import Image, ImageFilter

save_image = False


def gaussian_blur(fin="../images/fly1.jpg", fout="fly1_blur.jpg"):
    if fin == "" or fout == "":
        raise SyntaxError("No parameter")

    image = mpimg.imread(fin)
    blurred = filters.gaussian(image, sigma=1, multichannel=True)
    mpimg.imsave(fout, blurred)


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


print("len(sys.argv) =", len(sys.argv), sys.argv)

if (len(sys.argv) >= 2):
    target_dir = sys.argv[1]
else:
    target_dir = "../images/group/"


imagefiles = [f for f in listdir(target_dir) if isfile(join(target_dir, f))]

print(target_dir, imagefiles)
files = ["../images/fly1.jpg", "../images/fly2.jpg"]

images = []
edges = []

for i, file_name in enumerate(imagefiles):
    images.append(mpimg.imread(target_dir + file_name))

print("Image files = ", len(images))

for i, image in enumerate(images):
    print("[{i}]".format(i=i), imagefiles[i])
    fig = plt.figure()
    ax = fig.add_subplot(2, 2, 1)
    ax.set_title("Original")
    plt.axis("off")
    plt.imshow(image)

    edge = filters.sobel(image)
    ax = fig.add_subplot(2, 2, 2)
    ax.set_title("Edge(Orig)")
    plt.axis("off")
    plt.imshow(rgb2gray(edge))

    blurred = filters.gaussian(image, sigma=1, multichannel=True)
    if save_image:
        mpimg.imsave("result-01.jpg", blurred)
    ax = fig.add_subplot(2, 2, 3)
    ax.set_title("Blur(Orig)")
    plt.imshow(blurred)

    edge = filters.sobel(blurred)
    edges.append(edge)
    if save_image:
        mpimg.imsave("result-02.jpg", edge)
    ax = fig.add_subplot(2, 2, 4)
    ax.set_title("Edge(Blurred)")
    plt.axis("off")
    plt.imshow(rgb2gray(edge))

#    plt.show(block=False)
#    plt.pause(3)
    fig.savefig("debug-{i}.png".format(i=i))

# debug part
height = images[0].shape[0]
width = images[0].shape[1]
print("Image size", images[0].size, "= (", height, "x", width, ") x 3")

print("image", images[0].shape)
print("edge", edges[0].shape)

for i in range(height):
    for j in range(width):
#        for k in range(len(images)):
        if get_gray(edges[0][i][j]) > get_gray(edges[1][i][j]):
            image[i][j] = images[0][i][j]
        else:
            image[i][j] = images[1][i][j]


mpimg.imsave("result.jpg", image)

png0 = Image.open("result.jpg")
png0.save("result.png");
