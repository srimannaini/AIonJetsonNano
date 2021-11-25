import cv2                                        #importing library
import numpy as np                                #importing library
print(cv2.__version__)                            #printing version of library
evt=-1
coord=[]                                          #create array of pnts
img=np.zeros((250,250,3),np.uint8)                #creating frame
def click(event,x,y,flags,params):                #define click fun
    global pnt
    global evt    
    if event==cv2.EVENT_LBUTTONDOWN:              #event for left click
        print('Mouse Event Was: ',event)          #print the event
        print(x,',',y)                            #print x & y
        pnt=(x,y)                                 
        coord.append(pnt)                         #append to array
        evt=event                                 
    if event==cv2.EVENT_RBUTTONDOWN:
            print(x,y)
            blue=frame[y,x,0]                     #blue value of pixel
            green=frame[y,x,1]
            red=frame[y,x,2]
            print(blue,green,red)
            colorString=str(blue)+','+str(green)+','+str(red)        
            img[:]=[blue,green,red]              #matrix
            fnt=cv2.FONT_HERSHEY_PLAIN
            r=255-int(red)
            g=255-int(green)
            b=255-int(blue)
            tp=(b,g,r)                           #tuple
            cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
            cv2.imshow('myClor',img)
dispW=640                #width of window or display
dispH=480                #height of window
flip=2                   #if we dont flip we see images ups and down
cv2.namedWindow('piCam')
cv2.setMouseCallback('piCam',click)
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'            #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s
cam= cv2.VideoCapture(camSet)                                             #create camera object so if you want to work with camera use cam object
while True:                                                               #to read frames of camera
    ret, frame = cam.read()                                               #reads a frame, ret returns a variable 0 or 1, other is images we give it to frame variable
    for pnts in coord:                                                                                        
            cv2.circle(frame,pnts,5,(0,0,255),-1)                         #draw circle
            font=cv2.FONT_HERSHEY_PLAIN                                   #fornt type
            myStr=str(pnts)                                               #type conversion
            cv2.putText(frame,myStr,pnts,font,1.5,(255,0,0),2)            #text of pnt
    cv2.imshow('piCam',frame)                       #shows the frame in window piCam
    cv2.moveWindow('piCam',0,0)                     #move window to particular location
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break0
    if keyEvent==ord("c"):                    
        coord=[]                                    #clear the coardinated
cam.release()
cv2.destroyAllWindows()
