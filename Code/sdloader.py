# -*- encoding: utf-8 -*-
#SD Auto Loader - Enric Gómez Pitarch & Marc Cobler
#BCN3D Technologies - Fundacio CIM

#This Program lets you to copy the files you want to multiple SD Cards
#It has 4 rocker switches to select the folders and documents to upload and
#a load button to start the sequence. First it checks if there is internet
#to pull updates from Github and be updated all time.

import RPi.GPIO as GPIO
import time
import os
import subprocess as sub
import sys
import socket
from clint.textui import colored

BCN3DSigmaPath = "/home/pi/BCN3DSigma"
BCN3DPlusPath = "/home/pi/BCN3DPlus"
BCN3DSigmaScreenPath = "home/pi/BCN3DSigmaScreen"
repoPath = "/home/pi/sd-auto-loader"
codePath = "/home/pi/sd-auto-loader/Code"

#Tuple that holds all the input options of the software
inputOptions = ['sync','help']

#Pin declarations
LED1 = 21
LED2 = 20
LED3 = 16
LED4 = 12
LED5 = 7
LED6 = 8
LED7 = 25
LED8 = 24
LED9 = 23

def haveInternet():
	os.system("sudo ifup eth0")
	REMOTE_SERVER = "www.google.com"
	try:
		host = socket.gethostbyname(REMOTE_SERVER)
		s = socket.create_connection((host, 443))
		return True
	except:
		pass
	return False

def syncGithub():
	#Update the Repo
	if haveInternet():
		print (colored.green("=========Internet is ON!==========="))
		try:
			print "Getting updates from Github"
			os.chdir(repoPath)
			currentDirectory = os.getcwd()
			print "The current directory is: %s" % currentDirectory
			os.system("git pull origin master")
		except:
			print "Something went wrong, check your internet connection"
			pass
	else:
		print (colored.red("=============No internet, no github sync============="))

def manageInputs():
	print "Setting the switches to inputs"
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	#Set pull-ups to pins
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#Read inputs just one time
	input_state_5 = GPIO.input(5)
	input_state_26 = GPIO.input(26)
	input_state_19 = GPIO.input(19)
	input_state_13 = GPIO.input(13)
	input_state_6 = GPIO.input(6)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED1, GPIO.OUT)
	GPIO.setup(LED2, GPIO.OUT)
	GPIO.setup(LED3, GPIO.OUT)
	GPIO.setup(LED4, GPIO.OUT)
	GPIO.setup(LED5, GPIO.OUT)
	GPIO.setup(LED6, GPIO.OUT)
	GPIO.setup(LED7, GPIO.OUT)
	GPIO.setup(LED8, GPIO.OUT)
	GPIO.setup(LED9, GPIO.OUT)

def turnOnLED(pin):
	#print "turning on led: %d" % pin
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.1)

def turnOffLED(pin):
	#print "turning off led: %d" % pin
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.1)

def turnOffAllLEDs():
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)

def turnOnAllLEDs():
	GPIO.output(21, GPIO.HIGH)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(25, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)

def blinkLED(LED):
	turnOnLED(LED)
	time.sleep(0.25)
	turnOffLED(LED)

def startUpLEDS(times):
	#Just a sequence of LEDs to know that the system is running the program
	print "Lightning some LEDs..."
	for x in range(0,times):
		print ".	.	.	.	."
		turnOnLED(LED1)
		turnOnLED(LED2)
		turnOnLED(LED3)
		turnOnLED(LED4)
		turnOnLED(LED5)
		turnOnLED(LED6)
		turnOnLED(LED7)
		turnOnLED(LED8)
		turnOnLED(LED9)
		time.sleep(0.2)
		turnOffLED(LED9)
		turnOffLED(LED8)
		turnOffLED(LED7)
		turnOffLED(LED6)
		turnOffLED(LED5)
		turnOffLED(LED4)
		turnOffLED(LED3)
		turnOffLED(LED2)
		turnOffLED(LED1)
		#GPIO.cleanup()

def loadBCN3DSigmaSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen(['./formatAndCopy.sh', 'Sigma'])
	while (proc.returncode == None):
		turnOnAllLEDs()
		time.sleep(0.5)
		turnOffAllLEDs()
		proc.poll()
	if (proc.returncode != 0):
		print (colored.red("*************An error ocurred loading SD's***********"))
		turnOffAllLEDs()
	else:
		print (colored.green("----------------SD's Loaded Successfully!-----------------"))
		turnOnAllLEDs()
	time.sleep(2) #Sleep for 2 seconds
	for x in range(0,5):
		turnOnAllLEDs()
		time.sleep(0.25)
		turnOffAllLEDs()


def loadBCN3DSigmaScreenSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen(['./formatAndCopy.sh', 'LCD'])
	while (proc.returncode == None):
		turnOnAllLEDs()
		time.sleep(0.5)
		turnOffAllLEDs()
		proc.poll()
	if (proc.returncode != 0):
		print (colored.red("*************An error ocurred loading SD's***********"))
		turnOffAllLEDs()
	else:
		print (colored.green("----------------SD's Loaded Successfully!-----------------"))
		turnOnAllLEDs()
	time.sleep(2) #Sleep for 2 seconds
	for x in range(0,5):
		turnOnAllLEDs()
		time.sleep(0.25)
		turnOffAllLEDs()

def loadBCN3DPlusSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen(['./formatAndCopy.sh', 'Plus'])
	while (proc.returncode == None):
		turnOnAllLEDs()
		time.sleep(0.5)
		turnOffAllLEDs()
		proc.poll()
	if (proc.returncode != 0):
		print (colored.red("*************An error ocurred loading SD's***********"))
		turnOffAllLEDs()
	else:
		print (colored.green("----------------SD's Loaded Successfully!-----------------"))
		turnOnAllLEDs()
	time.sleep(2) #Sleep for 2 seconds
	for x in range(0,5):
		turnOnAllLEDs()
		time.sleep(0.25)
		turnOffAllLEDs()

def loadBCN3DRSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen(['./formatAndCopy.sh', 'R'])
	while (proc.returncode == None):
		turnOnAllLEDs()
		time.sleep(0.5)
		turnOffAllLEDs()
		proc.poll()
	if (proc.returncode != 0):
		print (colored.red("*************An error ocurred loading SD's***********"))
		turnOffAllLEDs()
	else:
		print (colored.green("----------------SD's Loaded Successfully!-----------------"))
		turnOnAllLEDs()
	time.sleep(2) #Sleep for 2 seconds
	for x in range(0,5):
		turnOnAllLEDs()
		time.sleep(0.25)
		turnOffAllLEDs()

def printButtonStatus():
	print "Switch 1 is set to: %d" % GPIO.input(6)
	print "Switch 2 is set to: %d" % GPIO.input(13)
	print "Switch 3 is set to: %d" % GPIO.input(19)
	print "Switch 4 is set to: %d" % GPIO.input(26)

def checkButtons(channel):
	#Read the status of the switches and buttons
	try:
		print "Reading the switch buttons..."
		input_state_26 = GPIO.input(26)
		input_state_19 = GPIO.input(19)
		input_state_13 = GPIO.input(13)
		input_state_6 = GPIO.input(6)
		printButtonStatus()

		if input_state_26 == False and input_state_19 == True and input_state_13 == True and input_state_6 == True:
			print 'Loading BCN3D Sigma SD'
			loadBCN3DSigmaSD()
			time.sleep(2)
		if input_state_26 == True and input_state_19 == False and input_state_13 == True and input_state_6 == True:
			print 'Loading BCN3D Sigma Display uSD'
			loadBCN3DSigmaScreenSD()
			time.sleep(2)
		if input_state_26 == True and input_state_19 == True and input_state_13 == False and input_state_6 == True:
			print 'Loading BCN3D+ SD'
			loadBCN3DPlusSD()
			time.sleep(2)
		if input_state_26 == True and input_state_19 == True and input_state_13 == True and input_state_6 == False:
			print 'Loading BCN3DR SD'
			loadBCN3DRSD()
			time.sleep(2)
		if input_state_26 == False and input_state_19 == False and input_state_13 == False and input_state_6 == False:
			turnOffAllLEDs()
			for x in range(0,5):
				turnOnAllLEDs();
				time.sleep(0.25);
				turnOffAllLEDs();
			print "Powering OFF The system"
			GPIO.cleanup()
			os.system("sudo poweroff")
		#if input_state_26 == True and input_state_19 == True and input_state_13 == True and input_state_6 == False:
	except KeyboardInterrupt:
		#If we press ctrl + c
		print "Program closed by user"
		GPIO.cleanup()
		sys.exit()
	except:
		print "Other error or exception ocurred!"
		GPIO.cleanup()
		sys.exit()


def printHelp():
	#function that prints the options available as input commands
	try:
		print "This are the available options: "
		print '\n'
		i = 0
		for option in inputOptions:
			print "#%d option" % i

		print '\n'
		print "Use: sudo python sdloader.py [OPTION]"
	except KeyboardInterrupt:
		#If we press ctrl + c
		print "Program closed by user"
		GPIO.cleanup()
		sys.exit()

#------------------------------------MAIN FLOW-----------------------------
def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == inputOptions[0]:
			syncGithub()
			#Only sync then quit
			sys.exit()
		elif sys.argv[1] == inputOptions[1]:
			printHelp()
			#When a keyboard is detected, exit program
		elif len(sys.argv) > 1 and sys.argv[1] not in inputOptions:
			#When input arguments are wrong
			print "command/s " + str(sys.argv[1:]) + " not recognised. Please type " + sys.argv[0] + " \"help\" to see commands"
			time.sleep(3)
			sys.exit()
	else:
		syncGithub()
		manageInputs()
		startUpLEDS(3)
		#Callback function in PIN 5. Whenever a Falling Edge is detected, run checkButtons function
		GPIO.add_event_detect(5, GPIO.FALLING, callback=checkButtons, bouncetime=150)
		while True:
			time.sleep(0.5)
			#print "waiting for the load button..."


#Just the regular boilerplate to start the program
if __name__ == '__main__':
	main()
