import os
import pickle
import cv2
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/background.png")

# importing mode images
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# load the encoding file
print("Loading encode file...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentsIds = encodeListKnownWithIds
# print(encodeListKnown)
print("encode file Loaded...")

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 360, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]
    # cv2.imshow("Webcam", img)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches", matches)
        print("facedis", faceDis)

    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# def rescale_frame(frame, percent=75):
#     scale_percent = 75
#     width = int(frame.shape[1] * scale_percent / 100)
#     height = int(frame.shape[0] * scale_percent / 100)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
