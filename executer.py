import moter
import requests
import time

serverURL = "http://rails-beanstalk.gb6ktuimmz.ap-northeast-2.elasticbeanstalk.com/push/device"

class Executer:
    def __init__(self, tcpServer, arduinoSerial):
        self.andRaspTCP = tcpServer
        self.m = moter.Moter()
        self.arduino = arduinoSerial
        
    def startCommand(self, command):
        
        if command == "w\n":
            self.m.rotate_left()

        elif command == "d\n":
            self.m.rotate_right()

        elif command == "x\n":
            self.arduino.send_signal('x')

        elif command == "y\n":
            self.arduino.send_signal("y")
            
        elif command == "o\n":
            self.arduino.send_signal("o")

        elif command == "c\n":
            self.m.rotate_right()
            #self.arduino.send_signal("c")
        
        elif command == 'a':
            res = requests.post(serverURL, data={'did':'raspberry002', 'signal':'a'})
            #self.andRaspTCP.sendAll("a\n")
            print(res.text)
