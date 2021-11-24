import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=320              #width of window or display
dispH=240                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object

PL=cv2.imread('pl.jpg')
PL=cv2.resize(PL,(75,75))
cv2.imshow('LogoWindow',PL)
cv2.moveWindow('LogoWindow',700,0)

PLGray=cv2.cvtColor(PL,cv2.COLOR_BGR2GRAY)
cv2.imshow('PLGray',PLGray)
cv2.moveWindow('PLGray',800,0)

_,BGMask=cv2.threshold(PLGray,250,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',900,0)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',1000,0)

FG=cv2.bitwise_and(PL,PL,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',1100,0)

BW=75
BH=75
Xpos=10
Ypos=10
dX=1
dY=1

while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable


    ROI=frame[Ypos:Ypos+BH,Xpos:Xpos+BW]
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow('ROIBG',ROIBG)
    cv2.moveWindow('ROIBG',1200,0)

    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',1300,0)
    frame[Ypos:Ypos+BH,Xpos:Xpos+BW]=ROInew

    Xpos=Xpos+dX
    Ypos=Ypos+dY

    if Xpos+BW>=dispW or Xpos<=0:
        dX=dX*(-1)
    if Ypos<=0 or Ypos+BH>=dispH:
        dY=dY*(-1)

    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of cameraq
cv2.destroyAllWindows()               #destroys all windows
