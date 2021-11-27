import face_recognition #library
import cv2
print(cv2.__version__)
image=face_recognition.load_image_file('/home/nvidia/Desktop/Jetson/pyPro/faceRecognizer/demoImages/unknown/u3.jpg') #load img into face reco lib
face_locations=face_recognition.face_locations(image)   #find faces using face rec lib
print(face_locations)                                  
image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
for (row1,col1,row2,col2) in face_locations:
    cv2.rectangle(image,(col1,row1),(col2,row2),(255,0,0),3)
cv2.imshow('myWindow',image)
cv2.moveWindow('mywindow',0,0)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllwindows()
    