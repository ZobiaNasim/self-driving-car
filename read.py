import cv2 as cv
#reading image
'''img=cv.imread('photo/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)'''

#reading videos
capture=cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0XFF==ord('d'):#if d is presed than video will stop playing
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)       
