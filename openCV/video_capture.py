import cv2, time

video = cv2.VideoCapture(0)

a = 1

while True:
    a = a + 1
    check, frame = video.read()
    #print (frame)
    bw_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capture', bw_img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#print(num)
video.release()
cv2.destroyAllWindows()