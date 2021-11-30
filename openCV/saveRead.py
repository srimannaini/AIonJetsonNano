import cv2               #importing library
print(cv2.__version__)   #printing version of library
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=120/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink' #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s,
cam= cv2.VideoCapture(camSet)
#cam= cv2.VideoCapture('videos/myCam.avi')
outVid=cv2.VideoWriter('videos/myCam1.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH)  )
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(1)     #create camera objects
while True:
    ret, frame = cam.read()     #read frames
    cv2.imshow('nanoCam',frame) 
    cv2.moveWindow('nanoCam',0,0)
    outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):  #change time b/w frame by changing waitkey attributes
        break
cam.release()
outVid.release()
cv2.destroyAllWindows()