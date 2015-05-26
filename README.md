# SD Auto Loader
All of our 3D printers come with an 8GB SD card with all the documentation needed to get ready and start printing.
All the info takes about half a gigabyte and a takes about 4 minutes to upload. Too much time. So we decided to do something about it and try to automate the process a little bit.

##How it works
We've taken a Raspberry Pi and plug it a 10 port USB hub. Then we throw in 8 SD Readers and we can start copying files.
The script detects the SD cards plugged and formats them before loading the files. Everything with a push of a button.

##Bill of materials
The list of things you'll need to replicate this project:
* 1x Raspberry Pi. We've used a Model B+ but any will fit. 
* 1x 5V power supply
* 8x SD card Readers
* Acces to a 3D Printer

Optionally we've included a wifi dongle to access the raspberry via SSH if needed to do some maintenance.
The total cost of the project is about 60€ including the raspberry.

##Code
The code is made in Python and you can download from the repository. We've configured the raspberry in order to run the script just after the powerup. You can follow [this instructions](http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/auto-running-programs) to do that.
You'll also need to configure the raspberry to start without login like [here](http://stackoverflow.com/questions/17830333/start-raspberry-pi-without-login).
If you want to do some wireless maintenance you'll need to configure the ssh server too. This is [how it's done](https://www.raspberrypi.org/documentation/remote-access/ssh/).

##Printed Parts
You can download all the **STL** files if you want to print our design or make your own.
The files are: 
* SDbottom.stl
* SDBoxTOP.stl


##Milestones






