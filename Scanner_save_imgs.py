import numpy as np
import cv2
from imutils.perspective import four_point_transform

#ISO 216, 300 dpi
width = 2480
height = 3508

#preprocessing
doc = cv2.imread("doc4.jpg")    #original image
scale = cv2.resize(doc, (width, height))    #resized
copy = scale.copy()
copy1 = scale.copy()
copy2 = scale.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)   #convert to grayscale
cv2.imwrite('Final images doc4/gray.jpg', gray)
blur = cv2.GaussianBlur(gray, (7, 7), 0)    #gaussian blur
cv2.imwrite('Final images doc4/blur.jpg', blur)
can = cv2.Canny(blur, 50, 250)  #edge detection
cv2.imwrite('Final images doc4/canny.jpg', can)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(can,kernel,iterations = 1)
cv2.imwrite('Final images doc4/dilated.jpg', dilation)

#processing
contours, _ = cv2.findContours(can, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #finding contours
sort = sorted(contours, key=cv2.contourArea, reverse=True)  #sorting by area
cv2.drawContours(copy2, sort, 0, (0,255,0), 12)
cv2.imwrite('Final images doc4/contour.jpg', copy2)
cv2.drawContours(copy1, sort, -1, (255,0,0), 12)
cv2.imwrite('Final images doc4/all_contours.jpg', copy1)
peri = cv2.arcLength(sort[0], True) #getting perimeter of document contour
approx = cv2.approxPolyDP(sort[0], 0.05 * peri, True) #getting 4 corners

cv2.circle(copy2, ((approx[0])[0]), radius=30, color=(0, 0, 255), thickness=15)
cv2.circle(copy2, ((approx[1])[0]), radius=30, color=(0, 255, 0), thickness=15)
cv2.circle(copy2, ((approx[2])[0]), radius=30, color=(255, 0, 0), thickness=15)
cv2.circle(copy2, ((approx[3])[0]), radius=30, color=(255, 0, 255), thickness=15)
cv2.imwrite('Final images doc4/corners.jpg', copy2)
#4 point transform
#warped = four_point_transform(scale, approx.reshape(4,2))
#warped = cv2.resize(warped, (2480, 3508))

#warp perspective
a4 = np.float32(np.array([[0,0], [0, height], [width, height], [width, 0]]))    #define corners of output image
corners = np.float32(approx)
perspectiveMatrix=cv2.getPerspectiveTransform(corners,a4)   #generating perspective matrix
warped=cv2.warpPerspective(scale, perspectiveMatrix, (width, height))   #creating bird-eye view #final8
cv2.imwrite('Final images doc4/bird_eye.jpg', warped)
#post processing
b_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)   #converting to grayscale
b_blur = cv2.medianBlur(b_gray, 5)  #reducing noise
binary = cv2.adaptiveThreshold(b_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)    #converting to binary
cv2.imwrite('Final images doc4/final.jpg', binary)  #exporting final output