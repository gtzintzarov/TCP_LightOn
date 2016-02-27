#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




# This creates the speaker class
class Speaker:
	def __init__(self, _pin):
		self.pin = _pin
		GPIO.setup(_pin, GPIO.OUT) #set the pin

	def playSound(self, frequency, duration):
		tempSpeaker = GPIO.PWM(self.pin,frequency)
		tempSpeaker.start(30) #50 is max volume
		time.sleep(duration)	#duration of note, in seconds
		tempSpeaker.stop()