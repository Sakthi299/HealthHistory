
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
        
        #cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        return barcodeData

def scanqrcode():
    cap = cv2.VideoCapture(2)
    while True:
        ret, frame = cap.read()
        a = decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            return a
            
            















'''
t0 = time.time() # start time in seconds

cap = cv2.VideoCapture(0)
while(True):
   ret, frame = cap.read()
   # ... processing or preview
   t1 = time.time() # current time
   num_seconds = t1 - t0 # diff
   if num_seconds > 30:  # e.g. break after 30 seconds
      break  
'''
