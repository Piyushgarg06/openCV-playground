import numpy as np
import cv2 as cv

blank = np.zeros((400,400),dtype='uint8')
cv.imshow('blank',blank)

rectangle = cv.rectangle(blank.copy(),(40,40),(360,360),(255,255,255),thickness=-1)
circle = cv.circle(blank.copy(),(200,200),200,(255,255,255),thickness=-1)

cv.imshow('circle',circle)
cv.imshow('rectangle',rectangle)

# bitwise AND used for only the intersecting points
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('and',bitwise_and)

# bitwise OR used for both intersecting and non-intersecting regions 
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('or',bitwise_or)

# bitwise XOR used for only the non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',bitwise_xor)

cv.waitKey(0)