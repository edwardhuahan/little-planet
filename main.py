import cv2 as cv
import numpy as np
import math

img = cv.imread("sampleDownsized.jpg")

if img is None: 
    print("Could not load image")

bwimg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

height, width = bwimg.shape

rowCount = 0
z = 0
direction = 1
for rows in bwimg:
    scaled = (2*(z/height))
    direction = 1
    if scaled > 1:
        scaled = (scaled*-1)+2
        direction = -1
    z = math.sqrt(1-scaled**2)*direction
    
    colCount = 0
    for column in rows:
        if (z != 1.0):
            mappingX = int(round((colCount*2)/(1-z)))
            mappingY = int(round((rowCount*2)/(1-z)))
            mapped[mappingX,mappingY] = column

        colCount += 1

    rowCount+=1

#cv.imshow("Display window", bwimg)



# Keep image up
#k = cv.waitKey(0)

#if k == ord("s"):
 #   cv.imwrite("sample.jpg", img)
