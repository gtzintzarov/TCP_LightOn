#! /usr/bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18,392)
pwm.start(50)
time.sleep(.2)
pwm.stop()
time.sleep(.2)
pwm = GPIO.PWM(18,587)
pwm.start(50)
time.sleep(.2)
pwm.stop()
time.sleep(.2)
pwm = GPIO.PWM(18,830)
pwm.start(50)
time.sleep(.6)
pwm.stop()
