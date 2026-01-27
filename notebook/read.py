import cv2 as cv
img = cv.imread("data/Photos/cat.jpg")
# cv.imshow('cat',img)
# cv.waitKey(0)

# capture = cv.VideoCapture("data/Videos/kitten.mp4")
# while True:
#     isTrue,frame = capture.read()
#     if not isTrue:
#         break
#     cv.imshow("cat",frame)
#     if cv.waitKey(1000) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
print(img.shape)
