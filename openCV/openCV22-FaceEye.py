import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
face_cascade=cv2.CascadeClassifier('/home/nvidia/Desktop/Jetson/pyPro/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/home/nvidia/Desktop/Jetson/pyPro/cascade/eye.xml')
while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.circle(roi_color,(int(xEye+wEye/2),int(yEye+hEye/2)),8,(255,0,0),-1)
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)       #move window
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows