import cv2

imagepath="C:\\Users\\sukmlt\\OneDrive - SAS\\Documents\\Learning\\Personal\\opencv\\sas-marlow.jpg"
#imagepath="C:\\Users\\sukmlt\\OneDrive - SAS\\Pictures\\ht.jpg"

#coloured image
img = cv2.imread (imagepath,1)

#B&W image
img1 = cv2.imread (imagepath,0)

#print matrix of image
print (img1)

#print type of matrix (which is numpy array)
print(type(img1))

#print size of image
print(img1.shape)

#display image
cv2.imshow("mel", img)
cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows()

resized = cv2.resize(img, (200,400))
resized2 = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

#display image
cv2.imshow("mel", resized2)
cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows()



