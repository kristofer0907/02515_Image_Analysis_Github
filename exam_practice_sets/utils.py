from skimage.morphology import erosion, dilation, opening, closing
from skimage.morphology import disk
import numpy as np
from skimage import color, io
import cv2
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu

def compute_outline(bin_img):
    """
    Computes the outline of a binary image
    """
    
    footprint = disk(1)
        
    dilated = dilation(bin_img, footprint)
        
    outline = np.logical_xor(dilated, bin_img)
        
    return outline

# From https://scikit-image.org/docs/stable/auto_examples/applications/plot_morphology.html
def plot_comparison(original, filtered, filter_name, x_dimension, y_dimension):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(x_dimension, y_dimension), sharex=True, sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(filter_name)
    ax2.axis('off')
    io.show()