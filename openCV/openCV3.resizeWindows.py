import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'   #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s,
cam=cv2.VideoCapture(camSet)                           #create camera object "cam" so if you want to work with camera use cam object
while True:                                            #to read frames of camera
    ret, frame=cam.read()                              #read a frame, ret returns a variable 0 or 1, other is images we give it to frame variable
    cv2.imshow('piCam',frame)                          #shows the frame in window piCam
    cv2.moveWindow('piCam',700,0)                      #move window to particular location
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)        #create a new frame "gray"  & convert color of frame from BGR to gray
    
    frameSmall=cv2.resize(frame,(320,240))             #resize window to particular size
    graySmall=cv2.resize(gray,(320,240))               #resize window to particular size
    cv2.imshow('BW',graySmall)                         #shows the frame in window BW
    cv2.imshow('piSmall',frameSmall)                   #shows the frame in window piSmall
    cv2.moveWindow('BW',0,265)                         #move window to particular location
    cv2.moveWindow('piSmall',0,0)                      #move window to particular location
    if cv2.waitKey(1)==ord('q'):                       #to quit the window
        break                                          #we break while loop
cam.release()                                          #let go of camera
cv2.destroyAllWindows()                                #destroys all windows
