import cv2               #importing library
print(cv2.__version__)   #printing version of library
import numpy as np
def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
cv2.createTrackbar('hueLow','Trackbars',50,179,nothing)
cv2.createTrackbar('hueUp','Trackbars',100,179,nothing)
cv2.createTrackbar('hueLow2','Trackbars',50,179,nothing)
cv2.createTrackbar('hueUp2','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)



dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    #frame=cv2.imread('smarties.png')  #read image in directory
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)      #convert to hsv image
    
    hueLow=cv2.getTrackbarPos('hueLow','Trackbars')
    hueUp=cv2.getTrackbarPos('hueUp','Trackbars')

    hueLow2=cv2.getTrackbarPos('hueLow2','Trackbars')
    hueUp2=cv2.getTrackbarPos('hueUp2','Trackbars')

    Ls=cv2.getTrackbarPos('satLow','Trackbars')
    Us=cv2.getTrackbarPos('satHigh','Trackbars')

    Lv=cv2.getTrackbarPos('valLow','Trackbars')
    Uv=cv2.getTrackbarPos('valHigh','Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    l_b2=np.array([hueLow2,Ls,Lv])
    u_b2=np.array([hueUp2,Us,Uv])

    #print(l_b,u_b)

    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,410)

    FG=cv2.bitwise_and(frame,frame,mask=FGmaskComp)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',480,0)

    BgMask=cv2.bitwise_not(FGmaskComp)
    cv2.imshow('bgMask',BgMask)
    cv2.moveWindow('bgMask',480,410)

    BG=cv2.cvtColor(BgMask,cv2.COLOR_GRAY2BGR)

    final=cv2.add(FG,BG)
    cv2.imshow('final',final)
    cv2.moveWindow('final',900,0)



    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows