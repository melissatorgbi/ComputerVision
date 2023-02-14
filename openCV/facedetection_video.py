import cv2, time

# Load the cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

a = 1

while True:
    a = a + 1
    check, frame = video.read()
    #print (frame)
    bw_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(bw_img, 1.1, 4)
# Draw rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Capture', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#print(num)
video.release()
cv2.destroyAllWindows()