'''
import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
while True:                           #to read frames of camera
    ret, frame=cam.read()             #read a frame returns a variable 0 or 1, other is images we give it to frame variable
    roi=frame[50:250,200:400]         #only certain part of window
    cv2.imshow('ROI',roi)             #show roi window
    cv2.imshow('piCam',frame)         #shows the frame in window piCam
    cv2.moveWindow('ROI',705,0)       #move to loc
    cv2.moveWindow('piCam',0,0)       #move to loc
    if cv2.waitKey(1)==ord('q'):      #to quit the window
        break                         #we break while loop
cam.release()                         #let go of camera
cv2.destroyAllWindows()               #destroys all windows
'''



import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame=cam.read()
    roi=frame[50:250,200:400].copy()                    #only certain part of window
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)        #convert color of frame
    roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)    #change color of certain position
    frame[50:250,200:400]=roiGray
    cv2.imshow('ROI',roi)
    cv2.imshow('nanoCam',frame)
    cv2.imshow('GRAY',roiGray)
    cv2.moveWindow('GRAY',705,250)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
