import cv2 as cv

img = cv.imread('face4.jpg')

x,y,w,h = 100,100,100,100

cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)

cv.circle(img,center=(x+w, y+h), radius=100, color=(255,0,0), thickness=5)

cv.imshow('re_img', img)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.waitKey(0)

cv.destroyAllWindows()