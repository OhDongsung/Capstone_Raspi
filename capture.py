import numpy as np
import cv2
import time
import requests

serverURL = "http://rails-beanstalk.gb6ktuimmz.ap-northeast-2.elasticbeanstalk.com/push/device"

while True:
    #faceCascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier('/home/pi/face.xml')
    image = cv2.imread('/home/pi/Pictures/pic.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
    )
    time.sleep(1)
    if len(faces) >= 1:
        cv2.imwrite('/home/pi/Pictures/captured.jpg', image)
        files = open("/home/pi/Pictures/captured.jpg", 'rb')
        upload = {'file':files}
        string = {'did':'raspberry002', 'signal':'d'}
        res = requests.post(serverURL , files = upload, data = string)
        print "face detected"
        print res.text
        time.sleep(9)
        faces = None
