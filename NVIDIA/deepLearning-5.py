
import jetson.inference
import jetson.utils
import time
import cv2
timeStamp=time.time()
fpsFilt=0
dispW=1280
dispH=720
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=60/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW=1920
dispH=1080
#cam=jetson.utils.gstCamera(dispW,dispH,'0')
#display=jetson.utils.glDisplay()
while display.IsOpen():
    img,width,height=cam.CaptureRGBA()
    detections=net.Detect(img,width,height)
 #   display.RenderOnce(img,width,height)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt+.1*fps
    print(str(round(fps,1))+'fps')
