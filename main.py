import cv2

image = cv2.imread('asadd.png',1 )

print(type(image))
resized_image = cv2.resize(image,(1600,900))
cv2.imshow("board",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()