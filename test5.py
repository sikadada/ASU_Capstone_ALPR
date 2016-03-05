__author__ = 'StreetHustling'


from PIL import Image
import pytesseract
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os


img = cv2.imread('images/bogart.JPG', 0)

surf = cv2.SURF(400)

kp, des = surf.detectAndCompute(img, None)

print(len(kp))

print surf.hessianThreshold

surf.hessianThreshold = 10000

kp, des = surf.detectAndCompute(img, None)

print(len(kp))


img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

plt.imshow(img2),plt.show()