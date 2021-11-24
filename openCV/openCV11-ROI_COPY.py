import cv2               #importing library
print(cv2.__version__)   #printing version of library
goFlag=0                 #
def mouse_click(event,x,y,flags,params):    #function mouse click
    global x1,y1,x2,y2                      #global variable
    global goFlag                           #
    if event==cv2.EVENT_LBUTTONDOWN:
        x1=x                                #assigning to global variable
        y1=y
        goFlag=0
    if event==cv2.EVENT_LBUTTONUP:       
        x2=x
        y2=y
        goFlag=1
cv2.namedWindow('piCam')                        #define window picam
cv2.setMouseCallback('piCam',mouse_click)       #create mouse event listening to picam and when there is mouse click call fun
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object

while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    if goFlag==1:
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)    #create rec eith mouse clicks
        roi=frame[y1:y2,x1:x2]                                    #region of interest
        cv2.imshow('Copy ROI',roi)
        cv2.moveWindow('Copy ROI',705,0)
    cv2.moveWindow('piCam',0,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loopq
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows
