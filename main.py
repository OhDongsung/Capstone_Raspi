import tcpServer
import executer
import Queue
import time
import arduino
import requests
import subprocess

# Get ip addr
arg = 'ip route list'
p = subprocess.Popen(arg,shell = True, stdout = subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]

# Unique number of raspberry pi
dat = {'did':'raspberry002', 'ip':ipaddr}

# Server ID
serverURL = "http://rails-beanstalk.gb6ktuimmz.ap-northeast-2.elasticbeanstalk.com/regist"

# make public queue
commandQueue = Queue.Queue()

# init module
andRaspTCP = tcpServer.TCPServer(commandQueue, ipaddr, 1234)
andRaspTCP.start()
arduinoSerial = arduino.Arduino(commandQueue)
arduinoSerial.start()

# set module to executer
commandExecuter = executer.Executer(andRaspTCP, arduinoSerial)

# post raspby device id, ip
res = requests.post(serverURL, data = dat)
print(res.text)
while True:
    try:
        command = commandQueue.get()
        commandExecuter.startCommand(command)
    except:
        pass
