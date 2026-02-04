import cv2 as cv
import numpy as np

img = cv.imread('data/Photos/cat.jpg')

averaging = cv.blur(img,(3,3))
gausian = cv.GaussianBlur(img,(3,3),0)
median = cv.medianBlur(img,3)
bilateral = cv.bilateralFilter(img,5,15,15)

cv.imshow('gaussian',gausian)
cv.imshow('average',averaging)
cv.imshow('median',median)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)