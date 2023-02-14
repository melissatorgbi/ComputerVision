import cv2

imagepath="C:\\Users\\sukmlt\\OneDrive - SAS\\Documents\\Learning\\Personal\\CV\\opencv\\mel.jpg"
# Load the cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read image B&W
img = cv2.imread(imagepath)
# Read image B&W
#bw_img = cv2.imread(imagepath,0)
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect face
faces = cascade.detectMultiScale(bw_img, 1.1, 4)
# Draw rectangle around face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()

