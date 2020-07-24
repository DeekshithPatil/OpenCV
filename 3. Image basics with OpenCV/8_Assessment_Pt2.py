# Task: open the dog_backpack image in a winddow, and when clicked on it, you must draw a circle

import numpy as np
import cv2
import matplotlib.pyplot as plt


def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,0,255),3)



img = cv2.imread('dog_backpack.jpg')
cv2.namedWindow('my_sketch')
cv2.setMouseCallback('my_sketch', draw_circle)

while True:
    cv2.imshow('my_sketch', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
