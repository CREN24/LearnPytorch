import cv2 as cv

img = cv.imread('face1.jpg')

resize_img = cv.resize(img, dsize=(200, 200))

cv.imshow('img', img)

cv.imshow('resize_img', resize_img)

print('Not edit: ', img.shape)

print('Edit: ', resize_img.shape)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.waitKey(0)

cv.destroyAllWindows()