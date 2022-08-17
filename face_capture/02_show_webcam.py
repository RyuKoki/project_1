# 02_show_webcam.py
import cv2

# define width and height of image
image_width = 640
image_height = 480
# window object for previewing image from webcam
cv2.namedWindow( "Camera", cv2.WINDOW_AUTOSIZE )
# index of webcam
webcam_index = 0
# webcam object
capture = cv2.VideoCapture( webcam_index )
# set width and height for openCV
capture.set( cv2.CAP_PROP_FRAME_WIDTH, image_width )
capture.set( cv2.CAP_PROP_FRAME_HEIGHT, image_height )
# super loop for video capture and display on window
while (True):
    # get video capture
    ret, frame = capture.read()
    # display the video capture
    cv2.imshow( "Camera", frame )
    # waiting for user press input from keyboard
    command = cv2.waitKey(10)
    # if press 'q' from keyboard is to quit
    if command == ord('q'):
        print("Ending the program")
        break
    # if press 's' from keyboard is to save the picture
    elif command == ord('s'):
        print("Saving the image")
        cv2.imwrite( "test.jpg", frame )
