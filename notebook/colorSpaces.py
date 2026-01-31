import cv2 as cv
img = cv.imread('data/Photos/park.jpg')
cv.imshow('image',img)

# BGR to GRAYSCALE
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
cv.waitKey(0)