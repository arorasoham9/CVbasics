import cv2
import time as t

firstFrame = None


video = cv2.VideoCapture(0) # add file name in place of 0\

while True:
    check, frame = video.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey,(21,21),0)
    if firstFrame is None:
        firstFrame = grey
        continue

    delta_frames = cv2.absdiff(firstFrame,grey)


    thresh_delta = cv2.threshold(delta_frames, 30,255, cv2.THRESH_BINARY)[1] #more operations other than THRESH_BINARY are possible
    thresh_delta = cv2.dilate(thresh_delta,None, iterations = 3)
    #contoured_frame = cv2.drawContours(thresh_delta)
    (conts,_)  = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for i in conts:
        if cv2.contourArea(i) <1000:
            continue
        (x,y,w,h) = cv2.boundingRect(i)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Color Frame", frame)
    cv2.imshow("Capturing video", grey)
    cv2.imshow("delta",delta_frames)
    cv2.imshow("Threshold",thresh_delta)

    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
video.release()
cv2.destroyAllWindows()