import cv2 as cv
import numpy as np
#always first create a dummy image before writing on image
blank=np.zeros((500,500,3),dtype='uint8')#uint8 is the datatype of an image
'''cv.imshow('Blank',blank)               
#img=cv.imread('photo/cat.jpg')
#cv.imshow('Cat',img)


#1.point the image a certain color
blank[:]=0,255,0  #for whole page color
blank[200:300,300:400]=0,0,255  #for coloring a specific portion of image
cv.imshow('Green',blank)


#2.Draw a Rectangle and circle and line
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2) #for coloring the rectangle thickness =cv.FILLED
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,2500),thickness=3) #for coloring the rectangle thickness =cv.FILLED
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,250),thickness=cv.FILLED)
cv.imshow('Circle',blank)
cv.line(blank,(100,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=2)
cv.imshow('line',blank)'''


#write text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,color=(0,255,0),thickness=2)
cv.imshow('Text',blank)


cv.waitKey(0)