import cv2 as cv
import numpy as np 

img = cv.imread('data/Photos/park.jpg')
b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b,g,r])
b_merge = cv.merge([b,blank,blank])
g_merge = cv.merge([blank,g,blank])
r_merge = cv.merge([blank,blank,r])
cv.imshow('blue_merge',b_merge)
cv.imshow('green_merge',g_merge)
cv.imshow('red_merge',r_merge)

cv.waitKey(0)