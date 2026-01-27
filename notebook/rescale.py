import cv2 as cv
#rescale
def rescale(frame,scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#rescaled image
image_large = cv.imread('data/Photos/cat_large.jpg')
cv.imshow("cat_original",image_large)
cv.imshow("recaled_img",rescale(image_large))
cv.waitKey(0)

#rescaled video
capture = cv.VideoCapture("data/Videos/kitten.mp4")
while True:
    isTrue,frame = capture.read()
    if not isTrue:
        break
    cv.imshow("cat_original",frame)
    cv.imshow("cat_rescaled",rescale(frame))

    if cv.waitKey(1000) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
