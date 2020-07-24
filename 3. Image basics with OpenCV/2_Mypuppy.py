import cv2

img = cv2.imread('00-puppy.jpg')


while True:
    cv2.imshow('Puppy',img) #This command is used to display an image by using CV2
    
    
    if (cv2.waitKey(1) & 0xFF == 27): # 27 is the ascii value (in decimal notation) of Esc button. If it is pressed, break out of the loop.
        #here 1 indicates, wait for 1 milliseconds.
        break
        
cv2.destroyAllWindows()

    
    