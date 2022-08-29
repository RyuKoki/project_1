# face recognition from picture

import cv2
import numpy as np
from os import listdir
import sys, time # sys to receive input from terminal (system)

# function read image from folder sort_face_pic for use to compare face
def get_images(path, size):
	sub= 0
	images, labels= [], []
	people= []

	for subdir in listdir(path):   # from main folder --> Get each person's filename
		for image in listdir(path+ "/"+ subdir):    # from sub foler --> Get the filename of each person's image

			img= cv2.imread(path+"/"+subdir+"/"+image, cv2.IMREAD_GRAYSCALE) # read img and set img to gray color
			img= cv2.resize(img, size)  # resize the image
			images.append(np.asarray(img, dtype= np.uint8)) # metric array
			labels.append(sub)  # number of rounds (folder)
		people.append(subdir)   # name of each person's filename
		sub+= 1
    
    # images -> metric array, labels -> instead of folder number, people -> folder name 
	return [images, labels, people]   


if __name__== "__main__":
    # if number argument is not right print warning error 
	if len(sys.argv)!= 3:
		print("Wrong number of arguments! See the usage.\n")
		print("Usage: face_recognition.py <fullpath/images/folder> <fullpath/../predict>")
		sys.exit()

	[images, labels, people]= get_images(sys.argv[1], (256, 256))   # input argument 1
	labels= np.asarray(labels, dtype= np.int32)

	print("Initializing eigen FaceRecognizer and training...") 
	sttime= time.process_time() # set time before start
    
    # train with Eigen Face algorithm
	eigen_model= cv2.face.EigenFaceRecognizer.create() 
	eigen_model.train(images, labels)   
	print("\tCompleted training in "+ str(time.process_time()- sttime)+ " Secs!")   # print time train process 

    # begin the process of distinguishing faces
	for image_name in listdir(sys.argv[2]):
		try:
			color_image= cv2.imread(sys.argv[2]+ "/"+ image_name)   # read file input argument 2
			[x, y]= color_image.shape[:2]  
			x_factor= (float(y)/x)
			resize_y= 480   # resize to 480
            
            # color img to show when process complete
			color_image= cv2.resize(color_image, (int(resize_y* x_factor), resize_y))
            
            # gray img to detect and predict
			pre_image= cv2.imread(sys.argv[2]+ "/"+ image_name, cv2.IMREAD_GRAYSCALE)
			pre_image= cv2.resize(pre_image, (int(resize_y* x_factor), resize_y))
		except:
            # if can't read img or other error
			print("Couldn't read image. Please check the path to image file.")
			sys.exit()

        # use file .xml detect face (Haar Cascade)
		frontal_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        # detect face | bBoxes -> location x,y 
		bBoxes= frontal_face.detectMultiScale(pre_image, 
			scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), 
			flags = cv2.CASCADE_SCALE_IMAGE)

		for bBox in bBoxes:
			(p,q,r,s)= bBox
            # draw rectangle around the face 
			cv2.rectangle(color_image, (p,q), (p+r,q+s), (2,255,25), 2)

			pre_crop_image= pre_image[q:q+s, p:p+r] # crop only face go to process
			pre_crop_image= cv2.resize(pre_crop_image, (256, 256))
            
            # predict img from eigen model
			[predicted_label, predicted_conf]= eigen_model.predict(np.asarray(pre_crop_image))
            
            # show people name in terminal and in img with rectangle around the face 
			print("Predicted person in the image "+ image_name+ " : "+ people[predicted_label])
			box_text= format("Subject: "+ people[predicted_label])
			cv2.putText(color_image, box_text, (p-20, q-5), cv2.FONT_HERSHEY_PLAIN, 1.5, (5,205,2), 2)

		cv2.imshow("Win1", color_image) # show color image
		cv2.imshow("Win2", pre_crop_image)  # show crop image with gray color
		cv2.waitKey(0)  # wait for key event