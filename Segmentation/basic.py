import cv2 as cv
import numpy as np

image = cv.imread('shapes.png')

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

edged = cv.Canny(gray,30,150)
cv.imshow('canny edges',edged)
cv.waitKey(0)

contours, hierarchy = cv.findContours(edged,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.imshow('canny edges after contouring',edged)
cv.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

cv.drawContours(image, contours, -1, (0,255,0), 3)

cv.imshow('Contours', image)
cv.waitKey(0)
cv.destroyAllWindows()
