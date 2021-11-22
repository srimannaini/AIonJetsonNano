import cv2
print(cv2.__version__)
evt=-1
coord=[]
def click(event,x,y,flags,params):
    global pnt
    global evt    
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ',event)
        print(x,',',y)
        coord.append(pnt)
        print(coord)
        evt=event
dispW=640
dispH=480
flip=2
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    for pnts in coord:
            cv2.circle(frame,pnts)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break0
cam.release()
cv2.destroyAllWindows()