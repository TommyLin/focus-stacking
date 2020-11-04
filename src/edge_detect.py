#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import filters

def edge_detect(fin, fout):
    if fin == '' or fout =='':
        raise SyntaxError('No parameter')

    image=mpimg.imread(fin)

    edges = filters.sobel(image)
#    plt.imshow(edges, cmap='gray')
#    plt.show()

    mpimg.imsave(fout, edges)

#@pytest.mark.skip
#edge_detect(sys.argv[1], sys.argv[2])
