#! /usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




# This creates the speaker class
class LED:
	def __init__(self, _pin):
		self.pin = _pin
		GPIO.setup(_pin, GPIO.OUT) #set the pin

	def on(self):
		GPIO.output(_pin, GPIO.HIGH)

	def off(self):
		GPIO.output(_pin, GPIO.LOW)