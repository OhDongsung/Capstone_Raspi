import RPi.GPIO as GPIO
import time

pin_pwm = 18    # pwm pin number
frequency = 50  # frequency 50 Hz


class Moter:
    p = 0
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin_pwm, GPIO.OUT)
        self.p = GPIO.PWM(pin_pwm, frequency)
        self.p.start(0)

    def rotate_left(self):
        self.p.ChangeDutyCycle(2)
    def rotate_right(self):
        self.p.ChangeDutyCycle(11)
    def end(self):
        self.p.stop()
        GPIO.cleanup()

def test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_pwm, GPIO.OUT)
    p = GPIO.PWM(pin_pwm, frequency)
    p.start(0)

    
    print("rotate left")
    time.sleep(1)
    Moter.rotate_right()
    print("rotate right")
    time.sleep(1)

    p.stop()
    GPIO.cleanup()
#    except KeyboardInterrupt:
#        p.stop():
