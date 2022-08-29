# detect people face from picture
import cv2
import sys

# read file name that want to detect
imgpath = sys.argv[1]

# use file .xml detect face (Haar Cascade)
trainfile = "haarcascade_frontalface_default.xml"   # file train model
facecascade = cv2.CascadeClassifier(trainfile)      # for obj detect

# read image and convert image color to black and white
img = cv2.imread(imgpath)   # read image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to gray

# detect face
face = facecascade.detectMultiScale(
    img_gray,
    scaleFactor = 1.3,
    minNeighbors = 5,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

# show output face detect
print("Found {} faces!".format(len(face)))

# Draw a rectangle around the faces if detect
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show image and rec frame that detect face
cv2.imshow("frame", img)

cv2.waitKey(0) # wait for key event