import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frameOriginal = cap.read()
    if ret==True:
        frame = cv2.cvtColor(frameOriginal,cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame, 20, 0.01, 10)
        corners = np.int0(corners)

        for i in corners:
            x, y = i.ravel()
            cv2.circle(frameOriginal, (x, y), 4, (128, 64, 128), -1)

        # write the flipped frame
        out.write(frameOriginal)
        

        cv2.imshow('frame',frameOriginal)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()