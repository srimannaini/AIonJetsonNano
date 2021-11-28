import face_recognition
import cv2
import os
import pickle
print(cv2.__version__)

Encodings=[]       #array of arrays of encodings
Names=[]           #who they are?

image_dir='/home/nvidia/Desktop/Jetson/pyPro/faceRecognizer/demoImages/known'    #path to images folder
for root, dirs, files in os.walk(image_dir):                  #every file in known dir
    print(files)                                              #array of all files
    for file in files:
        path=os.path.join(root,file)                          #add filename to path
        print(path)                                
        name=os.path.splitext(file)[0]                        #name without .jpg
        print(name)                                           
        person=face_recognition.load_image_file(path)         #
        encoding=face_recognition.face_encodings(person)[0]   #arryt of multiple faces
        Encodings.append(encoding)                            
        Names.append(name)
print(Names)
with open('train.pkl','wb') as f:
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)