import cv2
import time as t

har_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

video = cv2.VideoCapture(0) # add file name in place of 0\

while True:
    check, frame = video.read()
    #print(check)
    #print(frame)

    faces = har_cascade.detectMultiScale(frame,
                                        scaleFactor=1.1, minNeighbors=10)
    print(faces)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)


    #t.sleep(10)

    cv2.imshow("Capturing video", frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
video.release()
cv2.destroyAllWindows()