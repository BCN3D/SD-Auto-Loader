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

BCN3DSigmaPath = "/home/pi/BCN3DSigma"
BCN3DPlusPath = "/home/pi/BCN3DPlus"
BCN3DSigmaScreenPath = "home/pi/BCN3DSigmaScreen"
repoPath = "/home/pi/sd-auto-loader"
codePath = "/home/pi/sd-auto-loader/Code"

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
		print "Internet is ON!"
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
		print "No internet, no github sync" 
		
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
	proc = sub.Popen("./sd1FAT32")
	while (proc.returncode == None):
		blinkLED(LED1)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED1)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED1)
	#SD1 END
	proc = sub.Popen("./sd2FAT32")
	while (proc.returncode == None):
		blinkLED(LED2)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED2)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED2)
	#SD2 END
	proc = sub.Popen("./sd3FAT32")
	while (proc.returncode == None):
		blinkLED(LED3)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED3)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED3)
	#SD3 END
	proc = sub.Popen("./sd4FAT32")
	while (proc.returncode == None):
		blinkLED(LED4)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED4)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED4)
	#SD4 END
	proc = sub.Popen("./sd5FAT32")
	while (proc.returncode == None):
		blinkLED(LED5)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED5)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED5)
	#SD5 END	
	proc = sub.Popen("./sd6FAT32")
	while (proc.returncode == None):
		blinkLED(LED6)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED6)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED6)
	#SD6 END	
	proc = sub.Popen("./sd7FAT32")
	while (proc.returncode == None):
		blinkLED(LED7)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED7)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED7)
	#SD7 END	
	proc = sub.Popen("./sd8FAT32")
	while (proc.returncode == None):
		blinkLED(LED8)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED8)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED8)
	#SD8 END 
	proc = sub.Popen("./sd9FAT32")
	while (proc.returncode == None):
		blinkLED(LED9)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED9)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED9)
	#SD9 END 
	time.sleep(5) #Sleep for 5 seconds
	turnOffAllLEDs()

def loadBCN3DSigmaScreenSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen("./sd1FAT16")
	while (proc.returncode == None):
		blinkLED(LED1)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED1)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED1)
	#SD1 END
	proc = sub.Popen("./sd2FAT16")
	while (proc.returncode == None):
		blinkLED(LED2)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED2)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED2)
	#SD2 END
	proc = sub.Popen("./sd3FAT16")
	while (proc.returncode == None):
		blinkLED(LED3)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED3)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED3)
	#SD3 END
	proc = sub.Popen("./sd4FAT16")
	while (proc.returncode == None):
		blinkLED(LED4)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED4)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED4)
	#SD4 END
	proc = sub.Popen("./sd5FAT16")
	while (proc.returncode == None):
		blinkLED(LED5)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED5)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED5)
	#SD5 END	
	proc = sub.Popen("./sd6FAT16")
	while (proc.returncode == None):
		blinkLED(LED6)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED6)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED6)
	#SD6 END	
	proc = sub.Popen("./sd7FAT16")
	while (proc.returncode == None):
		blinkLED(LED7)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED7)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED7)
	#SD7 END	
	proc = sub.Popen("./sd8FAT16")
	while (proc.returncode == None):
		blinkLED(LED8)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED8)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED8)
	#SD8 END 
	proc = sub.Popen("./sd9FAT16")
	while (proc.returncode == None):
		blinkLED(LED9)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED9)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED9)
	#SD9 END 	
	time.sleep(5) #Sleep for 5 seconds
	turnOffAllLEDs()

def loadBCN3DPlusSD():
	os.chdir(codePath)
	startUpLEDS(1)
	time.sleep(2)
	proc = sub.Popen("./sd1Plus")
	while (proc.returncode == None):
		blinkLED(LED1)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED1)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED1)
	#SD1 END
	proc = sub.Popen("./sd2Plus")
	while (proc.returncode == None):
		blinkLED(LED2)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED2)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED2)
	#SD2 END
	proc = sub.Popen("./sd3Plus")
	while (proc.returncode == None):
		blinkLED(LED3)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED3)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED3)
	#SD3 END
	proc = sub.Popen("./sd4Plus")
	while (proc.returncode == None):
		blinkLED(LED4)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED4)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED4)
	#SD4 END
	proc = sub.Popen("./sd5Plus")
	while (proc.returncode == None):
		blinkLED(LED5)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED5)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED5)
	#SD5 END	
	proc = sub.Popen("./sd6Plus")
	while (proc.returncode == None):
		blinkLED(LED6)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED6)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED6)
	#SD6 END	
	proc = sub.Popen("./sd7Plus")
	while (proc.returncode == None):
		blinkLED(LED7)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED7)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED7)
	#SD7 END	
	proc = sub.Popen("./sd8Plus")
	while (proc.returncode == None):
		blinkLED(LED8)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED8)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED8)
	#SD8 END 
	proc = sub.Popen("./sd9Plus")
	while (proc.returncode == None):
		blinkLED(LED9)
		proc.poll()
	if (proc.returncode != 0):
		print "An error ocurred loading SD1"
		turnOffLED(LED9)
	else:
		print "SD1 Loaded Successfully!"		
		turnOnLED(LED9)
	#SD9 END 	
	time.sleep(5) #Sleep for 5 seconds
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
			loadBCN3DSigmaSD()
			time.sleep(2)
		if input_state_26 == False and input_state_19 == False and input_state_13 == False and input_state_6 == False:
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
		
		
#Main program
def main():
	syncGithub()
	manageInputs()
	startUpLEDS(3)
	#Callback function in PIN 5. Whenever a Falling Edge is detected, run checkButtons function
	GPIO.add_event_detect(5, GPIO.FALLING, callback=checkButtons, bouncetime=300)

	while True:
		time.sleep(1)
		#print "waiting for the load button..."		

#Just the regular boilerplate to start the program
if __name__ == '__main__':
	main()
