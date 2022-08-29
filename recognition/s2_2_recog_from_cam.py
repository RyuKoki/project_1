# face recognition from live camera

import cv2
import numpy as np
import os
import sys, time

# function read image from folder sort_face_pic for use to compare face
def get_images(path, size):
    sub= 0
    images, labels= [], []
    people= []

    for subdir in os.listdir(path): # from main folder --> Get each person's filename
        for image in os.listdir(path+ "/"+ subdir): # from sub foler --> Get the filename of each person's image
            img= cv2.imread(path+"/"+subdir+"/"+image, cv2.IMREAD_GRAYSCALE)    # read img and set img to gray color
            img= cv2.resize(img, size)  # resize the image

            images.append(np.asarray(img, dtype= np.uint8)) # metric array
            labels.append(sub)  # number of rounds (folder)
        people.append(subdir)   # name of each person's filename
        sub+= 1

    # images -> metric array, labels -> instead of folder number, people -> folder name
    return [images, labels, people]

# detect face 
def detect_faces(image):   
    frontal_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # use file .xml detect face (Haar Cascade)
    # bBoxes -> location x,y
    bBoxes= frontal_face.detectMultiScale(image, scaleFactor=1.3, 
        minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)  
    return bBoxes

# train model with Eigen Face algorithm
def train_model(path):
    [images, labels, people]= get_images(sys.argv[1], (256, 256))   # input argument 1 --> folder picture for train
    labels= np.asarray(labels, dtype= np.int32)
    print("Initializing eigen FaceRecognizer and training...")
    sttime= time.process_time()
    # train process
    eigen_model= cv2.face.EigenFaceRecognizer_create()
    eigen_model.train(images, labels)
    print("\tCompleted training in "+ str(time.process_time()- sttime)+ " Secs!")
    return [eigen_model, people]    # eigen_model -> Pic have train, people -> folder name

if __name__== "__main__":
    # if number argument is not right print warning error
    if len(sys.argv)!= 2:
        print("Wrong number of arguments! See the usage.\n")
        print("Usage: face_detrec_video.py <fullpath/images/folder>")
        sys.exit()

    arg_one= sys.argv[1]    # input from folder picture for train
    eigen_model, people= train_model(arg_one)   # train model

    cap= cv2.VideoCapture(1)    # for video capturing from cameras (camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # camera frame width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # camera frame height

    box_text= "Name: "  # for show name in frame when have detect face

    while(True):
        # capture image
        ret, frame= cap.read()  # capture img frame-by-frame
        frame = cv2.flip(frame, 1) # flip camera in the y-axis (mirror)
       
        # convert image color
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.equalizeHist(gray_frame)

        bBoxes= detect_faces(gray_frame)    # detect face from camera

        for bBox in bBoxes:
            (p,q,r,s)= bBox
            cv2.rectangle(frame, (p,q), (p+r,q+s), (25,255,25), 2)  # Draw a rectangle around the faces if detect

            # crop only face picture and convert to gray color for go to process
            crop_gray_frame= gray_frame[q:q+s, p:p+r]   
            crop_gray_frame= cv2.resize(crop_gray_frame, (256, 256))
            
            # predict img from eigen model
            [predicted_label, predicted_conf]= eigen_model.predict(np.asarray(crop_gray_frame))
            
            # show people name in terminal and in img with rectangle around the face 
            cv2.putText(frame, box_text, (p-20, q-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (25,0,225), 2)
            box_text= format("Name: "+ people[predicted_label])

        cv2.imshow("Video Window", frame)   # show camera live recognition
       
        """if (cv2.waitKey(5) & 0xFF== 27):    # wait for key event
            break
"""
        # wait for key event
        command = cv2.waitKey(10)
        # if press 'q' -> exit program
        if command == ord('q'):
            print ("Ending program")
            break  # end program
    
        # if press 's' -> save the image
        elif command == ord('s'):
            print ("Saving image")
            cv2.imwrite("cam.jpg",frame)  # save image

    cv2.destroyAllWindows()
