import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
BW=int(.2*dispW)                      #width of box
BH=int(.2*dispH)                      #height of box
posX=10                               #pos of box in x-direction
posY=270                              #pos of box in y-direction
dx=2                                  #how many pixels box has to move in x
dy=2                                  #how many pixels box has to move in y
while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    roi=frame[posY:posY+BH,posX:posX+BW].copy()      #region of interest
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #convert color to gray
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)     #again convert back its color
    frame[posY:posY+BH,posX:posX+BW]=roi             #position the roi on the frame
    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),3)
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    posX=posX+dx                      #move window in x-dir
    posY=posY+dy                      #move window in y-dir
    if posX+BW>=dispW or posX<=0:     #if it hits edge it reverse its dir
        dx=dx*(-1)
    if posY+BH>=dispH or posY<=0:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows