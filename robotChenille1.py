import time
import RPi.GPIO as GPIO

from threading import Timer

class RepeatTimer():
    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

pg = GPIO.PWM(17, 100)  # channel=17 frequency=50Hz
pd = GPIO.PWM(22, 100)  # channel=17 frequency=50Hz

cam = GPIO.PWM(7, 100)

GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)

pg.start(0)
pd.start(0)


cam_left = 8
cam_right = 13
i = cam_left
cam.start(cam_left)
while i<cam_right: 
	cam.ChangeDutyCycle(cam_left+i)
	time.sleep(1)
	i = i+0.25

pg.stop()
pd.stop()
GPIO.cleanup()

