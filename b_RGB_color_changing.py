import cv2
import numpy as np
def nothing(x):
    pass
image = np.zeros((512, 512,3), np.uint8)
#cv2.imshow('image', image)
cv2.namedWindow('image')
cv2.createTrackbar('Red','image', 0, 255, nothing)
cv2.createTrackbar('Green','image', 0, 255, nothing)
cv2.createTrackbar('Blue','image', 0, 255, nothing)
switch= '0: OFF \n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while (1):
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF==27:
        break
    red= cv2.getTrackbarPos('Red', 'image')
    green= cv2.getTrackbarPos('Green', 'image')
    blue = cv2.getTrackbarPos('blue', 'image')
    s= cv2.getTrackbarPos(switch,'image')
    if s==1:
        image[:]=[blue, green, red]
cv2.destroyAllWindows()