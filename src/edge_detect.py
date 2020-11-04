#!/usr/bin/env python3

import sys
import matplotlib.image as mpimg
from skimage import filters

def edge_detect(fin = "../images/fly1.jpg", fout = "fly_edge.jpg"):
    if fin == "" or fout == "":
        raise SyntaxError('No parameter')

    image = mpimg.imread(fin)
    edges = filters.sobel(image)
    mpimg.imsave(fout, edges)

#@pytest.mark.skip
#edge_detect(sys.argv[1], sys.argv[2])
