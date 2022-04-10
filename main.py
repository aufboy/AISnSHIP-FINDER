import cv2
from ai import predict
import time
import matplotlib.pyplot as plt
from text_finder import finder
def camera_start(cap):
    rat, frame = cap.read()    
    cv2.imwrite('cam.png', frame)
    img = cv2.imread('cam.png')
    res = cv2.resize(img, (406, 462), cv2.INTER_NEAREST)
    cv2.imwrite(
        'cam.png', 
        res
    )
