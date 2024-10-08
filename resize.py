import cv2 as cv
img=cv.imread('photo/cat.jpg')
cv.imshow('Cat',img)
def rescaleFrame(frame,scale=0.2):#for rescaling images,videos and live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image) 

#only for resizing live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    

capture=cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0XFF==ord('d'):#if d is presed than video will stop playing
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)    