#! /usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




# This creates the speaker class
class LED:
	def __init__(self, _pin):
		self.pin = _pin
		GPIO.setup(self.pin, GPIO.OUT) #set the pin

	def on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def off(self):
		GPIO.output(self.pin, GPIO.LOW)