import cv2

har_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

img1 = cv2.imread('img3.jpeg');
igm1 = cv2.resize(img1,[1600,900])
gray_img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


faces =  har_cascade.detectMultiScale(gray_img1,
scaleFactor = 1.1, minNeighbors = 10)

for x,y,w,h in faces:
    img1 = cv2.rectangle(img1, (x,y),(x+w,y+h), (0,255,0),3)
print(faces)
print(type(faces))

cv2.imshow("image1gray",img1)
cv2.waitKey( )
cv2.destroyAllWindows()
