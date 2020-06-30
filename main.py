import cv2 as cv
import numpy as np
from scipy import interpolate
import math

def calcOffset (i,j):
    return i - j/2

def calcR (x,y):
    return np.sqrt(calcOffset(x,w)**2 + calcOffset(y,h)**2)

def calcRho (x,y):
    return np.divide(calcR(x,y),z)

def calcTheta (x,y):
    return 2 * np.arctan(calcRho(x,y))

def calcA (x,y):
    return np.arctan2(calcOffset(y,h),calcOffset(x,w))

img = cv.imread("sample.jpg")

img = cv.resize(img, (0,0), fx=0.10, fy=0.10)

if img is None: 
    print("Could not load image")

bwimg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

h, w = bwimg.shape
z = w
rads = 2*math.pi/w;

a = np.linspace(1,2,w)
b = np.linspace(1,2,h)

[pixX, pixY] = np.meshgrid(a,b)

lat = calcTheta(pixX,pixY)
lon = calcA(pixX,pixY) - math.pi/4

lat = np.mod(lat + math.pi, math.pi) - math.pi/2
lon = np.mod(lon + math.pi, math.pi*2) - math.pi

xe = w/2.0 - (-lon/rads)
ye = h/2.0 - (lat/rads)

outImage = np.zeros([h,w]);

#cv.imshow("Display window", bwimg)
outImage = interpolate.interp2d(xe,ye,bwimg,kind='cubic')



#Keep image up
#k = cv.waitKey(0)

#if k == ord("s"):
 #   cv.imwrite("sample.jpg", img)
