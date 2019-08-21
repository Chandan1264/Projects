import cv2,vlc
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
w = 1280
h = 1024

p=vlc.MediaPlayer('C:/Users/lenovo/Desktop/PythonProject/demo.mp3')
while True:
    k = 2
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        k = 1
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            k = 0
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    cv2.imshow("dd",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    if k is not 0:
        p.stop()
        k = 2
    else:
        p.play()
        k = 2
cap.release()
cv2.destroyAllWindows()
