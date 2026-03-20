import os
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom
import sys
class ballInHole():
    def __init__(self, hole_diameter = float): #hole_diameter in mm
        self.hole_diameter = hole_diameter
        self.image_path_folder = "/home/kkristjansson/DTU/spring2026/34755_dependableRobotSystems/images_new"

        print(f"Ball in hole mission initialized with hole diameter: {self.hole_diameter}")


    

    


if __name__ == "__main__":

    path_folder = "/home/kkristjansson/DTU/spring2026/34755_dependableRobotSystems/images_new/"
    files = [os.path.join(path_folder, f) for f in os.listdir(path_folder) if f.endswith(".jpg")] 

    for i in range(len(files)):
        im_org = io.imread(path_folder+files[i])
        io.imshow(im_org)
        plt.title("Metacarpal image")
        io.show()



    ballInHole(40.6)  # Example hole diameter