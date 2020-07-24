import cv2
import numpy as np

# Variables
drawing = False  # True while mouse button down. False while mouse button up
ix = -1
iy = -1  # used to hole position of mouse


# Function
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x, y  # When left button is clicked we need to start drawing so drawing = true and then record
        # current mouse location for start point of rectangle


    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


# Showing the Image


# Black Image

img = np.zeros((512, 512, 3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
