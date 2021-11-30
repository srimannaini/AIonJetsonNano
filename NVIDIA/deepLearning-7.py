import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np 

timeStamp=time.time()
fpsFilt=0
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW=1280
dispH=720
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX

# Gstreamer code for improvded Raspberry Pi Camera Quality
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=60/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
outVid=cv2.VideoWriter('videos/detect.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH)  )
#cam=jetson.utils.gstCamera(dispW,dispH,'0')

#cam=cv2.VideoCapture('/dev/video1')
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

#cam=jetson.utils.gstCamera(dispW,dispH,'/dev/video1')
#display=jetson.utils.glDisplay()
#while display.IsOpen():
while True:
    #img, width, height= cam.CaptureRGBA()
    _,img = cam.read()
    height=img.shape[0]
    width=img.shape[1]

    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson.utils.cudaFromNumpy(frame)

    detections=net.Detect(frame, width, height)
    #print(detections)
    for detect in detections:
        print(detect)
        ID=detect.ClassID
        top=int(detect.Top)
        left=int(detect.Left)
        bottom=int(detect.Bottom)
        right=int(detect.Right)
        item=net.GetClassDesc(ID)
        #print(item,top,left,bottom,right)
        tk=1
        if item=='cat':
            tk=-1
        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),1)
        cv2.putText(img,item,(left,top+20),font,.75,(0,0,255),1)
    #display.RenderOnce(img,width,height)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt + .1*fps
    #print(str(round(fps,1))+' fps')
    cv2.putText(img,str(round(fpsFilt,1))+' fps',(0,30),font,1,(0,0,255),2)
    cv2.imshow('detCam',img)
    cv2.moveWindow('detCam',0,0)
    outVid.write(img)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()