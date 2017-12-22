import serial
import threading
import time

class Arduino(threading.Thread):
    
    def __init__(self, commandQueue):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.commandQueue = commandQueue
        threading.Thread.__init__(self)
   
    def send_signal(self, sig):
        self.ser.write(sig)
    
    def run(self):
        while True:
            try:
                state = self.ser.read()
                print(state)
                if(state == 'a'):
                    self.commandQueue.put('a')
                    state = None
            except:
                pass

