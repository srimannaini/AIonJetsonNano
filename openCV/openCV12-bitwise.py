import cv2               #importing library
import numpy as np
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
img1=np.zeros((480,640,1),np.uint8)   #create image
img1[0:480,0:320]=[255]               #change color
img2=np.zeros((480,640,1),np.uint8)
img2[190:290,270:370]=[255]
bitAnd=cv2.bitwise_and(img1,img2)     #bitwise and for two images
bitOr=cv2.bitwise_or(img1,img2)     #bitwise and for two images
bitXor=cv2.bitwise_xor(img1,img2)     #bit wise and for two images
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    
    cv2.imshow('img1',img1)           #show image
    cv2.moveWindow('img1',0,500)
    cv2.imshow('img2',img2)           #show image
    cv2.moveWindow('img2',700,0)
    cv2.imshow('And',bitAnd)          #show image
    cv2.moveWindow('And',700,500)
    cv2.imshow('Or',bitOr)            #show image
    cv2.moveWindow('Or',1340,0)
    cv2.imshow('Xor',bitXor)           #show image
    cv2.moveWindow('Xor',1340,500)
    frame=cv2.bitwise_and(frame,frame,mask=bitXor)   #only shows where mask is white
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windowsq