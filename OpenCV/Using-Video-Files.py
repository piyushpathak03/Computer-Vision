import cv2
import time
cap = cv2.VideoCapture('vedio_file.mp4')

fps = 25

if cap.isOpened()== False: 
    print("Error opening the video file. Please double check your file path for typos. Or move the movie file to the same location as this script/notebook")
    

while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:
        

        time.sleep(1/fps)
        cv2.imshow('frame',frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            
            break

    else:
        break
        
cap.release()

cv2.destroyAllWindows()
