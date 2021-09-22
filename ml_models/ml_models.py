import tkinter as tk
from tkinter import messagebox
import cv2
import os
from PIL import Image #pip install pillow
import numpy as np    # pip install numpy
from datetime import datetime
import mysql.connector

            #CONNECTION TO THE DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="face_attendancesystem"
    )



def train_classifier():
 
    data_dir="datasets"
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                img = Image.open(path).convert('L')

                #CONVERTING THE IMAGE INTO NUMPY ARRAY
                imageNp = np.array(img, 'uint8')
                #GETTING THE USER ID ON THE IMAGE
                id = int(os.path.split(path)[1].split(".")[1])
        
            faces.append(imageNp)
            ids.append(id)
        
    ids = np.array(ids)
    
    # Train and save 
    #LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person
    classifier = cv2.face.LBPHFaceRecognizer_create()
    classifier.train(faces,ids)
    classifier.write("classifier.xml")
    messagebox.showinfo('Result','Training dataset completed!!!')












def generate_dataset(name,course,birthdate,gender,userType):

    connection = mydb.cursor()
    
    connection.execute("SELECT * from known_faces")
    myresult = connection.fetchall()

    id=1
    for x in myresult :
        id+=1

    sql= "insert into known_faces (face_id,name,course,birthdate,sex,userType) values (%s,%s,%s,%s,%s,%s)"
    val = (id,name,course,birthdate,gender,userType)

    connection.execute(sql,val)
    mydb.commit()




    face_classifier = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
    #If face is detected on camera it will capture it then convert into GRAYSCALE then finally cropped the frontal face
    def face_cropped(img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.5, 5)
        # scaling factor = 1.5
        # minimum neighbor = 5
        
        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h,x:x+w]
        return cropped_face
    
    cap = cv2.VideoCapture(0)
    img_id = 0
    folder_name= 'face.'+str(id)+"."+userType
    os.makedirs("datasets/"+folder_name)
    while True:
        ret, frame = cap.read()
        if face_cropped(frame) is not None:
            img_id+=1
            face = cv2.resize(face_cropped(frame), (300,300))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            #create folder
            file_name_path = "datasets/"+str(folder_name)+"/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (124,255,0), 2)
            
            cv2.imshow("Cropped face", face)
            
        #THE MAXIMUM VALUE OF DATASETS BEING GENERATE
        if cv2.waitKey(1)==13 or int(img_id)==200: #13 is the ASCII character of Enter
            break
            
    cap.release()
    messagebox.showinfo('RESULT','GENERATE DATASETS SUCCESSFULLY')








def start_faceRG(): 
    
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        
        for (x,y,w,h) in features:
            
            #DRAW A RECTANAGLE TO THE DETECTED FACE 
            cv2.rectangle(img, (x,y), (x+w,y+h), color, 2 )
            
            id, pred = clf.predict(gray_img[y:y+h,x:x+w])

            #FORMULA TO COMPUTE FOR CONFIDENCE
            confidence = int(100*(1-pred/300))






            cursor = mydb.cursor()     
            cursor.execute("select * from known_faces where face_id="+str(id))
            person = cursor.fetchall()
            #convert into string
         
            for row in person:
                name= row[1]
                course = row[4]
                userType = row[5]


            name = ''+''.join(name)
            course = ''+''.join(course)
            # section = ''+''.join(section)     



            #Confidence likelihood of the results being true
            threshold = 80
            if confidence>threshold :

                    cv2.putText(img, name+','+course, (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    cv2.putText(img,"Confidence: " + str(confidence), (x,y+180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    markAttendance(userType,name)
            
            else:
                cv2.putText(img, "UNAUTHORIZED", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
        
        return img




    def markAttendance(userType,name):
        with open('Attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S %p')
                date = now.strftime('%Y-%m-%d')
                f.writelines(f'\n{name},{time},{date},{userType}')
 
 
 
 
    # loading classifier
    faceCascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture = cv2.VideoCapture(0)

    #SETTINGS
    scaleVal = 1.2
    neigh =  7

    #This loop is for detecting and diplaying the object/face with rectangle 
    while True:
        ret, img = video_capture.read() 
        img = draw_boundary(img, faceCascade,scaleVal,neigh, (255,255,255), "Face", clf)
        cv2.imshow("face Detection", img)
        
        if cv2.waitKey(1)==13:
            break
    video_capture.release()
    cv2.destroyAllWindows()



