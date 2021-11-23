import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'   #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)                        #create camera object so if you want to work with camera use cam object
while True:                                         #to read frames of camera
    ret, frame=cam.read()                           #read a frame, ret returns a variable 0 or 1, other is images we give it to frame variable
    cv2.imshow('piCam',frame)                       #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)                     #move window to particular location
    cv2.imshow('piCam2',frame)                      #shows the frame in window piCam
    cv2.moveWindow('piCam2',640,0)                  #move window to particular location

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #create a new frame "gray"  & convert color of frame from BGR to gray
    cv2.imshow('grayVideo',gray)                    #shows the frame in other window
    cv2.moveWindow('grayVideo',0,520)               #put it at other location
    cv2.imshow('grayVideo2',gray)
    cv2.moveWindow('grayVideo2',640,520)
    if cv2.waitKey(1)==ord('q'):                    #to quit the window
        break                                       #we break while loop
cam.release()                                       #let go of camera
cv2.destroyAllWindows()                             #destroys all windows


