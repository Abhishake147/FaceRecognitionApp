import os
import cv2
import numpy as np
import face_recognition

path = 'C:/Users/crazy/PycharmProjects/ImageformProject/media/img/'
images = []
userNames = []
mylist = os.listdir(path)
print(mylist)
for obj in mylist:
    curImg = cv2.imread(f'{path}{obj}')
    images.append(curImg)
    userNames.append(os.path.splitext(obj)[0])
print(userNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodingKnownFaces = findEncodings(images)
print('Encoding Complete!!')



cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(frame)
    encodesCurFrame = face_recognition.face_encodings(frame, facesCurFrame)

    for faceloc,faceEncode in zip(facesCurFrame, encodesCurFrame):
        matches = face_recognition.compare_faces(encodingKnownFaces, faceEncode)
        faceDis = face_recognition.face_distance(encodingKnownFaces, faceEncode)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = userNames[matchIndex].upper()

            y1, x2, y2, x1 = faceloc
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(frame, (x1, y2-30), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1+5, y2+5), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(10) == ord('q'):  # wait until q is pressed
        break

cap.release()
cv2.destroyAllWindows


