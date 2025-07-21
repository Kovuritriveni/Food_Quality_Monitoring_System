import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory
import serial

ser=serial.Serial('com4',9600)

        #import tensorflow as tf
import numpy as np
from keras.preprocessing import image

from keras.models import load_model
new_model = load_model('model.h5')


import cv2

# Open the default camera
cam = cv2.VideoCapture(1)

while(1):
        ret, frame = cam.read()

       

        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            

            cv2.imwrite('test.jpg',frame)
            cv2.waitKey(1)
    
            test_image = image.load_img('test.jpg',target_size=(64,64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = new_model.predict(test_image)
            result1 = result[0]
            print(result1)
            for i in range(6):
        
                if result1[i] == 1.:
                    x=i
                    break;
            if x==0:
                prediction = 'Fresh Apple'
                ser.write('2'.encode())
            elif x == 1:
                prediction = 'Fresh Banana'
                ser.write('2'.encode())
            elif x == 2:
                prediction = 'Fresh Orange'
                ser.write('2'.encode())
            elif x == 3:
                prediction = 'Rotten Apple'
                ser.write('1'.encode())
            elif x == 4:
                prediction = 'Rotten Banana'
                ser.write('1'.encode())
            else:
                prediction = 'Rotten Orange'
                ser.write('1'.encode())
