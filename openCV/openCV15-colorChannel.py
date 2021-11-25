import cv2               #importing library
print(cv2.__version__)   #printing version of library
import numpy as np
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
blank=np.zeros([480,640,1],np.uint8)  #create blank img
#blank[0:240,0:320]=255

while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    #print(type(frame))
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(frame[50,45,2])              #pixel value
    #print(frame.shape)                #shape of each frame/gray 
    #print(frame.size)                 #num of pixels
    b,g,r=cv2.split(frame)
    blue=cv2.merge((b,blank,blank))    #shows only blue
    #print(blue[50,45,0])
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))
    b[:]=b[:]*2
    merge=cv2.merge((b,g,r))
    #b=cv2.split(frame)[0]            #only blue pixel
    #g=cv2.split(frame)[1]
    #r=cv2.split(frame)[2]
    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',700,0)
    cv2.imshow('green',green)
    cv2.moveWindow('green',0,500)
    cv2.imshow('red',red)
    cv2.moveWindow('red',700,500)
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    cv2.imshow('merge',merge)         #shows the frame in window piCam
    cv2.moveWindow('merge',1400,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows