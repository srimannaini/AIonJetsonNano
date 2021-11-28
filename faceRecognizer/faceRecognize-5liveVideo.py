import face_recognition
import cv2
import os
import pickle
print(cv2.__version__)
dispW=640                #width of window or display
dispH=480                #height of window
flip=2
Encodings=[]
Names=[]

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)

font=cv2.FONT_HERSHEY_SIMPLEX
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'    #string variable it launches gstreamer to run the camera, native width that's coming out of camera full resolution, 21 f/s, 
cam=cv2.VideoCapture(camSet)          #create camera object so if you want to work with camera use cam object

while True:
    _,frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB,model='cnn')
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)
    for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
        name='Unknown Person'
        matches=face_recognition.compare_faces(Encodings,face_encodings)
        if True in matches:
            first_match_index=matches.index(True)
            name=Names[first_match_index]
        top=top*4
        right=right*4
        bottom=bottom*4
        left=left*4
        cv2.rectangle(frame,(left,top),(bottom,right),(0,0,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(0,0,255),2)
    cv2.imshow('Picture',frame)
    cv2.moveWindow('Picture',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

    