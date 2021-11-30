import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np
width=1280
height=720
#cam=jetson.utils.gstCamera(width,height,'/dev/video1')
cam=jetson.utils.gstCamera(width,height,'0')
net=jetson.inference.imageNet('googlenet')
timeMark=time.time()   #grab clock
fpsFilter=0            #low pass filter
timeMark=time.time()
font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    frame, width, height = cam.CaptureRGBA(zeroCopy=1)    #makle sure to give w & h
    classID, confidence = net.Classify(frame, width, height)    #recognize image & gives confidence
    item = net.GetClassDesc(classID)                            #Know the object
    dt=time.time()-timeMark                                     #change in time 
    fps=1/dt                                                    #calc fps
    fpsFilter=.95*fpsFilter+.05*fps                             #
    timeMark=time.time()
    frame=jetson.utils.cudaToNumpy(frame,width,height,4)        #convert cuda2numpy
    frame=cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame,str(round(fpsFilter,1))+'      '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('webCam',frame)
    cv2.moveWindow('webCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()




'''
fps=20
no latency
google net image recogn model
tensorRT optimization
'''
