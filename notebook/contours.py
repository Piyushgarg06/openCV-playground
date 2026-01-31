import cv2 as cv
import numpy as np


img = cv.imread("data/Photos/cats.jpg")
# cv.imshow("cats",img)

blank1 = np.zeros(img.shape)
blank2 = np.zeros(img.shape)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("grey",grey)

canny = cv.Canny(img,125,175)
cv.imshow("canny",canny)

blur = cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

canny_blur = cv.Canny(blur,125,175)
cv.imshow("canny_blur",canny_blur)


contours,hierarchy = cv.findContours(grey,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"found {len(contours)} in the canny image")

contours_blur,hierarchy_blur = cv.findContours(canny_blur,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"found {len(contours_blur)} in the canny_blur image")

cv.drawContours(blank1,contours,-1,(0,0,255),1)
cv.drawContours(blank2,contours_blur,-1,(0,0,255),1)

cv.imshow('contour_canny',blank1)
cv.imshow('contour_canny_blur',blank2)

cv.waitKey(0)