import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'       #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s
cam=cv2.VideoCapture(camSet)                                       #create camera object so if you want to work with camera use cam object
dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))                       #display width from the camera
dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))                      #display height from the camera
BW=int(.25*dispW)                                                  #Box width
BH=int(.15*dispH)                                                  #Box height
posX=10                                                            #start position
posY=270                                                           #start y position
dx=2                                                               #how much we change when we go through each frame
dy=2                                                               #how much we change when we go through each frame
while True:                                                        #to read frames of camera
    ret, frame=cam.read()                                          #reads a frame, ret returns a variable 0 or 1, other is images we give it to frame variable
    cv2.moveWindow('nanoCam',0,0)                                  #move window to particular location
    frame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1)       #draw rectangle
    cv2.imshow('picCam',frame)                                     #shows the frame in window piCam
    posX=posX+dx                                                   #change position
    posY=posY+dy                                                   #change position
    if posX<=0 or posX+BW>=dispW:                                  #change direction
        dx=dx*(-1)
    if posY<=0 or posY+BH>dispH:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):                    #to quit the window
        break                                       #we break while loop
cam.release()                                       #let go of camera
cv2.destroyAllWindows()                             #destroys all windows