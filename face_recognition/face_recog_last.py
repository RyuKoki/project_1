# import library
import face_recognition as face
import cv2
import numpy as np

# Get a reference to webcam (camera index)
video_capture = cv2.VideoCapture(1)

# folder picture for train ( รอหาวิธีทำเป็น folder )
# 11-12 this is only picture
ry_image = face.load_image_file("D:/project_code/camera/recognition/sort_face_pic/cherry/396049.jpg")
ry_encoding = face.face_encodings(ry_image)[0]

# create arrays of face encoding and name for detect people
know_encodings = [ry_encoding]
know_name = ["Cherry"]

process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    if process_this_frame :
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # same as rgb_small_frame = small_frame[:, :, ::-1]
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)    
            
        # Find all faces and do face encodings in camera
        face_locations = face.face_locations(rgb_small_frame)
        face_encodings = face.face_encodings(rgb_small_frame, face_locations)
            
        face_names = []
        face_percents = []
        # compare face 
        for encoding in face_encodings :
            # face_distance return how similar of face
            face_distance = face.face_distance(know_encodings, encoding)
            best_match_index = np.argmin(face_distance)
            face_percent = 1-face_distance[best_match_index]

            # if similar > 65 % return name else = unknow
            if face_percent > 0.65 :
                name = know_name[best_match_index]
                percent = round(face_percent*100,2)
            else:
                name = "Unknow"
                percent = 0

            face_names.append(name)
            face_percents.append(percent)
    
    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name, percent in zip(face_locations, face_names, face_percents):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.putText(frame, str(percent), (left + 6, bottom+23), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
