# Contributors: Will Walbers, Kiril Kuzmanovski, Muhammed Imran Anthony Nepomuceno
# Publication Date: 2/28/2019
# Description: This program records video from webcam, converts it into LAB color space
# and outputs a video file.

import cv2
import sys
import numpy as np
import math
from skimage import io, color

def video_setup():
    # Create a VideoCapture object and get video from webcam
    # 0 for HD(if connected, otherwise internal), 1 for internal (if HD connected)
    cap = cv2.VideoCapture(0)
    cap.set(3,1920)
    cap.set(4,1080)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output2.avi',fourcc, 20.0, (1920,1080))

    # Create the haar cascade - used for lighting and stuff
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    return cap, faceCascade, out

def detect_faces(cap, faceCascade, out):
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            #frame[:,:] = [0,0,0]
            for (x, y, w, h) in faces:
                # L = 0
                # A = 0
                # B = 0
                # rows = 0
                # cols = 0
                # Draws rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                #cv2.rectangle(frame, (x,y), ())
                #forehead = frame[y:y+90, x:x+w]
                cv2.rectangle(frame, (x + int(w*.3), y+int(h*.1)), (x+ int(w*.7), y+int(h*.25)), (0,255,0),2)
                # gets forehead from image and turns into lab
                # face_frame = frame[y:y+h, x:x+w]
                # rgb_face = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
                # face_frame[:,:] = [30,0,0]
                # lab_face = color.rgb2lab(rgb_face)
                #
                # # Gets dimension of face_frame
                # rows = len(lab_face)
                # cols = len(lab_face[0])
                #
                # # Thresholds: 6N lounge, test_vid1, 2, and 3 = 7
                # threshold = 7
                # gain = 0.8
                # for i in range(rows):
                #     for j in range(cols):
                #         if((lab_face[i][j][1] > threshold)):
                #             # print(lab[i][j][1])
                #             face_frame[i][j][0] = 0
                #             face_frame[i][j][1] = 0
                #             # Colors red channel where 255 is light and 0 is darker
                #             face_frame[i][j][2] = 255 - (gain * lab_face[i][j][1]) * (255/25)


            # Saves frame to video output
            out.write(frame)
            # Displays frame
            cv2.imshow('Video', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            # If receiving input from file, then processes until exit key or has read all frames
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                break
        # Break the loop
        else:
            break
    return cap, out

def video_cleanup(cap, out):
    # When everything done, release the video capture object
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return
