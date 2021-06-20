# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:19:40 2021

@author: SHUB
"""

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, background = cap.read()
    
    cv2.imshow("Background",background)
    
    if(cv2.waitKey(1) == ord('q')):
        cv2.imwrite("background.jpg", background)
        break


cap.release()
cv2.destroyAllWindows()
