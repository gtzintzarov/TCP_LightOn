#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)




# This creates the speaker class
class Speaker:
	def __init__(self, _pin):
		self.pin = _pin
		GPIO.setup(_pin, GPIO.OUT) #set the pin

	def playSound(self, frequency, duration, volume):
		tempSpeaker = self.GPIO.PWM(self.pin,frequency)
		tempSpeaker.start(volume/100) #50 is max volume
		sleep(duration)	#duration of note, in seconds
		tempSpeaker.stop()