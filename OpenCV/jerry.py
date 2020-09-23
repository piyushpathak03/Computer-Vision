import cv2
img = cv2.imread('frame0.jpg')
while True:
    cv2.imshow('jerry',img)
    #if we have waited at least 1msec & we have pressed ESC key
    if cv2.waitKey(1) & 0xff == 27:
        break
cv2.destroyAllWindows()