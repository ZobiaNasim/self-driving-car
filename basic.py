import cv2 as cv
img=cv.imread('photo/cat.jpg')
cv.imshow('Cat',img)

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur (Gaussian blur)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)