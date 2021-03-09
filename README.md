# Project Title

This program recognize the shape of objets to sort them with a Niryo robot

## Getting Started

- This program is build to work with a raspberry pi 3+ and a raspberry pi camera<br/>
- Put the camera Pi on the arm of the robot with a 2m cable and connect it to the raspberry

### Prerequisites

System used :<br/> 
- Ubuntu 16.04 for test purposes<br/>
- Raspberry 3+ with Raspbian 4.14 and 5 inch 800 by 480 display<br/>

Plastic parts :<br/>
- Print them from the Pièce/V Gillet folder with mat black filament

### Installing

Installing pycharm on ubuntu :<br/>

	pycharm:
		sudo snap install pycharm-community --classic
	Packages: 
		Pillow
		numpy
		opencv-contrib-python
		opencv-python
		pip
		pymodbus
	

Install python3 and all require packages on the raspberry :

	python & pip:
		sudo apt-get update
		sudo apt-get -y upgrade
		sudo apt-get install python3-dev
		sudo apt-get install python3-pip
		sudo apt-get install -y python3-pip
	Modbus:
		pip3 install pymodbus
	OpenCV	
		sudo apt-get install libhdf5-dev libhdf5-serial-dev
		sudo apt-get install libqtwebkit4 libqt4-test
		sudo pip3 install opencv-contrib-python
		sudo pip3 install "picamera[array]"
		sudo pip3 install imutils
		sudo pip3 install pyautogui
		sudo apt-get install libatlas-base-dev
		sudo apt-get install libjasper-dev
		sudo apt-get install libqtgui4
		sudo apt-get install python3-pyqt5
	Tkinter
		apt-get install python3-tk
	Pillow
		sudo pip3 install Pillow
	numpy
		sudo apt-get install python3-numpy

## Start the program
To find the IP adress of the robot
- Find it with [Niryo One Studio](https://niryo.com/fr/telechargement/)

To prepare the robot
- Put the modbus_server.py from the Robot 6 axes/Communication Modbus/Serveur folder in the main folder of the robot (move it with SSH command)

To run the program from Raspbian:
- Change the IP adress of the robot in the NiryoVision.py file from the main folder
- Change the gorobot variable with True and goraspberry with True
- Put the NiryoVision.py, programme.sh and connexion.sh in the same folder on the raspberry
- Plug the robot and connect it to the network
- Run the connexion.sh script. If no error occur, the connexion is established successfully, leave the window open
- Run the programme.sh code and the code must be running with no error. If dont, install the require packages and check the ip adress<br/>

To run the program from Ubuntu:
- Change the IP adress of the robot in the NiryoVision.py file from the main folder
- Change the gorobot variable with True and goraspberry with False
- Plug the robot and connect it to the network
- Run the connexion.sh script. If no error occur, the connexion is established successfully, leave the window open
- Run the NiryoVision.py from Pycharm in python3 and it must be running with no error. If dont, install the require packages and check the ip adress
	
### Run the program in manual mode

- To run it in manual mode, go to the manual menu and move it to all the positions you want.

### Prepare the area

- To find all the points of the area, use the manual mode and mark all the points when moving the robot to all positions
- Find a white area for better results

### Run the program in automatic mode

- Place the parts to marked points and run the automatic mode. If the parts are not recognize, check the luminosity of the room your perform the test.


## Contributing

- openCV: (https://www.framboise314.fr/i-a-realisez-un-systeme-de-reconnaissance-dobjets-avec-raspberry-pi/)<br/>
- tkinter: (https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234859-creez-des-interfaces-graphiques-avec-tkinter)<br/>
- Documentation python: (https://docs.python.org/3/)<br/>
- Documentation .markdown: (https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/)<br/>
## Authors

* **Gillet Niels** - *Niryo communication and Graphical interface*
* **Hartman Nicolas** - *OpenCV*
* **Houba Guillaume** - *OpenCV and multithreading*



