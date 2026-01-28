import cv2 as cv
import numpy as np
img = cv.imread('data/Photos/park.jpg')
cv.imshow('park',img)


# translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)
# +x -- move right 
# -x -- move left
# -y -- move up
# +y -- move down
cv.imshow('translated',translate(img,30,30))

# Rotation
def Rotation(img,angle,rotPoint=None):
    height = img.shape[0]
    width = img.shape[1]
    if rotPoint==None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)
    return cv.warpAffine(img,rotMat,dimension)
    # +angle -- counterCLockWise
    # -angle -- clockWise

cv.imshow('rotated',Rotation(img,30))

# Flipping an image
cv.imshow('flip',cv.flip(img,-1))

cv.waitKey(0)