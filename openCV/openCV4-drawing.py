import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s,
cam=cv2.VideoCapture(camSet)                                                        #create camera object so if you want to work with camera use cam object
while True:                                                                         #to read frames of camera
    ret, frame=cam.read()                                                           #reads a frame, ret returns a variable 0 or 1, other is images we give it to frame variable
    frame=cv2.rectangle(frame,(340,100),(400,170),(0,255,0),4)                      #draws rectangle
    frame=cv2.circle(frame,(320,240),50,(255,0,255),-1)                             #draws circle
    fnt=cv2.FONT_HERSHEY_DUPLEX                                                     #type of font
    frame=cv2.putText(frame,'My First Text',(300,300),1,fnt,(255,0,150),2)          #text 
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)                               #draw a line
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(255,255,255),1)                  #draw arrow line
    cv2.imshow('piCam',frame)                       #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)                     #move window to particular location
    if cv2.waitKey(1)==ord('q'):                    #to quit the window
        break                                       #we break while loop
cam.release()                                       #let go of camera
cv2.destroyAllWindows()                             #destroys all windows
