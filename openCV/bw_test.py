import cv2

imagepath="C:\\Users\\sukmlt\\OneDrive - SAS\\Pictures\\ht.jpg"

#B&W image
img = cv2.imread (imagepath,0)

cv2.imwrite("C:\\Users\\sukmlt\\OneDrive - SAS\\Pictures\\ht.jpg",img)

#display image
cv2.imshow("test", img)
cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows()