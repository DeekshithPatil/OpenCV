import cv2
import numpy as np

################################
###FUNCTION#####################
################################
def draw_circle(event,x,y,flags,param): #These arguments are automatically filled when the Mouse Callback is executed and this function is called
    if event == cv2.EVENT_LBUTTONDOWN:
        print("inside")
        cv2.circle(img,(x,y),100,(0,255,0),-1) #draw a circle at the curent position of mouse with radius 100 pixels, color = green and solid (i.e fill)

img = np.zeros((512,512,3),np.int8)
cv2.namedWindow(winname='my_drawing') #This command is used to open a window with the following name
cv2.setMouseCallback('my_drawing',draw_circle) #This command works on the 'my_drawing' window and passess the mouse values to the function draw_circle

#NOTE: All the windows, i.e namedWindow, setMouseCallback and imshow, all are acting on the same window, 'my_drawing'



################################
###SHOWING IMAGE WITH OPNECV####
################################



while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey() & 0xFF == 27:
        break

cv2.destroyAllWindows()