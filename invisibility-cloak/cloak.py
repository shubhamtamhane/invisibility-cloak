# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:19:40 2021

@author: SHUB
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

background = cv2.imread('./background.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    
    if(ret==False):
        break
    
    hue_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow("Hue Frame", hue_frame)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv2.inRange(hue_frame, lower_blue, upper_blue)
    #cv2.imshow("Mask", mask)
    
    part1 = cv2.bitwise_and(background, background, mask=mask)
    #cv2.imshow("Part1", part1)
    
    mask_inv = cv2.bitwise_not(mask)
    
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    #cv2.imshow("Part2", part2)
    
    cv2.imshow("Cloak", part1+part2)
    
    
    
    if(cv2.waitKey(1) == ord('q')):
        break
    

cap.release()
cv2.destroyAllWindows()

