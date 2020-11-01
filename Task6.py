#Task 6 - Kernels
#Transformation Notes
#Code written by Laura Whelan on 18/10/2020

#==========================================
#This code opens an image, builds a kernel for the image, and applies the filter to the image. 
#==========================================

#import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#1. Open image 
I = cv2.imread("Orange.png")

#2. Build a kernel for sharpening an image (researched) and apply filter to the image
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
F = cv2.filter2D(I, -1, kernel)

cv2.imshow("Orange",I)
cv2.imshow("kernel applied",F)


#Advanced Task: subtract the filtered image from the original to highlight changes
S = cv2.subtract(I,F)
cv2.imshow("Subtracted",S)
key =cv2.waitKey(0)