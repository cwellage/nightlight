from counterfit_connection import CounterFitConnection
import cv2

CounterFitConnection.init('127.0.0.1', 5000) 
cap = cv2.VideoCapture(0)
frame_count = 0 

def LitLED(faceCount):
        # Check whether user selected camera is opened successfully.
        if  faceCount>0:
                CounterFitConnection.set_actuator_boolean_value(1,1)            
                CounterFitConnection.set_actuator_boolean_value(0,0)
        else  :
                CounterFitConnection.set_actuator_boolean_value(0,1);  CounterFitConnection.set_actuator_boolean_value(1,0)

try :
        while True:
        # Read a frame from the camera
                isopend = cap.isOpened()
                ret, frame = cap.read()

        # Display the frame
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                if face_cascade is not None:
                        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))
                        frame_count = len(faces)
                        cv2.imshow('cam',frame)
                        LitLED(frame_count)
        # Break the loop if 'q' key is pressed
                if (cv2.waitKey(1) & 0xFF == ord('q')):
                        break
except Exception as e :
        raise e 


