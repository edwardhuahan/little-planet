import cv2 as cv
import numpy as np
from scipy import interpolate
import math

def calcOffset (i,j):
    return i - j/2

def calcR (x,y):
    return np.sqrt(calcOffset(x,width)**2 + calcOffset(y,height)**2)

def calcRho (x,y):
    return np.divide(calcR(x,y),length)

def calcTheta (x,y):
    return 2 * np.arctan(calcRho(x,y))

def calcLongitude (x,y):
    return np.arctan2(calcOffset(y,height),calcOffset(x,width))

img = cv.imread("sample.jpg")

if img is None: 
    print("Could not load image")

img = cv.normalize(img.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)

#img = cv.resize(img, (int(round((img.shape[1]*0.05))),int(round((img.shape[0]*0.05)))))
width = img.shape[1]
height = img.shape[0]
radians = 2*math.pi/width;
length = width/10

x = np.arange(1,width+1)
y = np.arange(1,height+1)

[a, b] = np.meshgrid(x,y)
latitude = calcTheta(a,b)
longitude = calcLongitude(a,b) - math.pi/4
latitude = np.mod(latitude + math.pi, math.pi) - math.pi/2
longitude = np.mod(longitude + math.pi*2, math.pi*2) - math.pi

Xq = width/2.0-(-longitude/radians)
Yq = height/2.0-(latitude/radians)

output = np.zeros([height,width,3]);

# apply transformation to red green and blue channels separately
for i in range(0,3):
    f = interpolate.RectBivariateSpline(x,y,img[:,:,i].T)
    output[:,:,i]= f(Xq, Yq,grid=False)

cv.imshow("Display",output)

k = cv.waitKey(0)

cv.waitKey(0) # waits until key is pressed
cv.destroyAllWindows() # destroys window
