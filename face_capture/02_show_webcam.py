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

