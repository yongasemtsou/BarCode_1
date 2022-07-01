import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

#img = cv2.imread('multiple.png')
#code = decode(img)
#print(code)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(3,480)
used_codes = []

#Use Webcam to reade BarCode
while True:
    success, img =cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData=barcode.data.decode('utf8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts= pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(255,0,255),2)

    
    cv2.imshow('Result', img)
    key = cv2.waitKey(15)

    if key == ord('q'):
        break
