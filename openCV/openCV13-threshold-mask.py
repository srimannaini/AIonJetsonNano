import cv2               #importing library
print(cv2.__version__)   #printing version of library

####add track bar ####
def nothing():
    pass
cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue','Blended',50,100,nothing)

dispW=320                #width of window or display
dispH=240                #height of window
flip=2                   #if we dont flip we see images ups and down


cvLogo=cv2.imread('cv.jpg')                #read image form directory
cvLogo=cv2.resize(cvLogo,(320,240))        #resize image
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)    #convert color
cv2.imshow('cv Logo Gray',cvLogoGray)                 #show image
cv2.moveWindow('cv Logo Gray',0,250)                  #move window


_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY) #_ is unused variable
cv2.imshow('BGMask',BGMask)                 #show image
cv2.moveWindow('BG Mask',330,0)           #move window


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object


while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    

    BG=cv2.bitwise_and(frame,frame,mask=BGMask)  #background mask
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',670,0)

    FGMask=cv2.bitwise_not(BGMask)
    cv2.imshow('FG Mask',FGMask)
    cv2.moveWindow('FG Mask',1000,250)

    FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',1330,250)

    compImage=cv2.add(BG,FG)
    cv2.imshow('compImg',compImage)
    cv2.moveWindow('compImg',660,250)

    BV=cv2.getTrackbarPos('BlendValue','Blended')/100
    BV2=1-BV


    Blended=cv2.addWeighted(frame,BV,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',1017,0)

    FG2=cv2.bitwise_and(Blended,Blended,mask=FGMask)
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1324,0)

    compFinal=cv2.add(BG,FG2)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',330,250)

    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows