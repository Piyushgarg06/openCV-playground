import cv2 as cv
img = cv.imread('data/Photos/cats 2.jpg')
# cv.imshow('color',img)

# #converting an image to greyscale
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grey',grey)

# #bluring an image
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("blurred",blur)

# #edge cascading
# canny = cv.Canny(img,125,175)
# cv.imshow('edges',canny)

# #dilating an image 
# dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('dilate',dilated)

# #erosion
# eroded = cv.erode(canny,(7,7),iterations=1)
# cv.imshow('eroded',eroded)

#resizing
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',resized)

#cropping
cropped = img[50:200,200:350]
cv.imshow('cropped',cropped)
cv.waitKey(0)


