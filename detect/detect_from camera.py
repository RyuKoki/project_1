# detect people face from live camera
import cv2
from cv2 import VideoCapture

cam = cv2.VideoCapture(1)    # for video capturing from cameras (camera_index)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # set frame height

# use file .xml detect face (Haar Cascade)
trainfile = "haarcascade_frontalface_default.xml"   # file train model
facecascade = cv2.CascadeClassifier(trainfile)      # for obj detect

while(True):
    # capture image
    ret, frame = cam.read() # capture img frame-by-frame
    frame = cv2.flip(frame, 1)  # flip camera in the y-axis (mirror)

    # convert image color
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert image to gray

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
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # show image and rec frame that detect face
    cv2.imshow("detect feom camera", frame)

    # wait for key event
    command = cv2.waitKey(10)
    # if press 'q' -> exit program
    if command == ord('q'):
        print ("Ending program")
        break  # end program
 
    # if press 's' -> save the image
    elif command == ord('s'):
        print ("Saving image")
        cv2.imwrite("detect_cam.jpg",frame)  # save image

        img = cv2.imread('detect_from_cam.jpg')   
        cv2.imshow('image',img)  # show image

# return resources
cam.release()
cv2.destroyAllWindows()