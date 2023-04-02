import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img, "Sun", (100,130), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color =(255, 255, 255))
cv2.putText(img, "Mercury", (120,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color =(255, 255, 255))
cv2.putText(img, "Venus", (200,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color =(255, 255, 255))
cv2.putText(img, "Earth", (300,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color =(255, 255, 255))
cv2.putText(img, "Mars", (400,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color =(255, 255, 255))
cv2.putText(img, "Jupitar", (600,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color =(255, 255, 255))
cv2.putText(img, "Saturn", (800,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color =(255, 255, 255))
cv2.putText(img, "Uranus", (1000,150), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color =(255, 255, 255))
cv2.putText(img, "Neptune", (1200,180), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color =(255, 255, 255))


cv2.imshow('output', img)
cv2.waitKey(0)
