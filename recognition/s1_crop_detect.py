# detect image and crop face then save
# this file save the crop image for train model

import cv2
from os import listdir  # for list file name
import time

# crop image 
def cropImage(img, box):
	[p, q, r, s]= box
	write_img_color= img[q:q+ s, p:p+ r]
	saveCropped(write_img_color, name)

# save crop image
def saveCropped(img, name):
	cv2.imwrite(output_path+ name, img)

if __name__== "__main__":

	input_path= "face_pic/input/"   # sub folder in main floder that have picture for traim
	output_path= "face_pic/output/" # sub folder in main floder that want to save crop image

    # use file .xml detect face (Haar Cascade)
	frontal_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	input_names= listdir("D:/project_code/camera/recognition/"+ input_path) # main folder location

	print("Starting to detect faces and save the cropped images to output file...")
	sttime= time.process_time()	# set time before run

	for name in input_names:    #loop for do all image in folder
		print(input_path+name)
		color_img= cv2.imread(input_path+ name) # read image
		gray_img= cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)   # convert image to gray

        # detect face
		bBoxes= frontal_face.detectMultiScale(
            gray_img, 						
            scaleFactor=1.3, 				
            minNeighbors=5, 				
            minSize=(30, 30), 				
            flags = cv2.CASCADE_SCALE_IMAGE	
        )

		for box in bBoxes:  # crop only face detect
			cropImage(color_img, box)

	print("Completed the task in %.2f Secs." % (time.process_time()- sttime))	# show time process

