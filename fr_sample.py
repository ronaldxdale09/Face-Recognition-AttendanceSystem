import cv2
import numpy as np
import os
from datetime import datetime
import face_recognition

path= 'ImagesAttendance'
images= []
personName = []
myList = os.listdir(path)
print(myList)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    personName.append(os.path.splitext(cls)[0])

print(personName)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        encode  = face_recognition .face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodingCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)


    for encodeFace, faceLoc in zip(encodingCurFrame,faceCurFrame):
        matches =face_recognition.compare_faces (encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        matchIndex = np.argmin(faceDis)

        if faceDis[matchIndex] < 0.50:
            name = personName[matchIndex].upper()
            markAttendance(name)
        else:
            name = ''
        # print(name)
        y1, x2, y2, x1 = faceLoc
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)


    cv2.imshow('CCTV',img)
    cv2.waitKey(1)


# faceLoc = face_recognition.face_locations(imgDale)[0]
# encodeDale = face_recognition.face_encodings(imgDale)[0]
# cv2.rectangle(imgDale, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([encodeDale], encodeTest)
# faceDis = face_recognition.face_distance([encodeDale], encodeTest)