import gphoto2 as gp #NOT NECESSARY
import subprocess
from time import sleep
import serial

# file-selector
f = open("cameraAPI/text.txt","r")
	

# serial setup
laserElectronics = serial.Serial(
	port = '/dev/ttyACM0',
	baudrate = 9600,
	timeout = 5
)

# transmit to Arduino
for line in f:
	laserElectronics.write(line.encode())
	sleep(2)
f.close()

while(laserElectronics.in_waiting < 3):
        continue

response = (laserElectronics.read(laserElectronics.in_waiting).decode())

#this funtions uses terminal to auto detect attached camera
def detect_cam():
	detect = subprocess.Popen(["gphoto2", "--auto-detect"], stdout=subprocess.PIPE)
	print detect.communicate()[0] + "Connection Successful"

#the iso setting variable has to be one of the array position; 
#[100,200,400,800,1600,3200,6400,12800,25600] -> [0,1,2,3,4,5,6,7,8]
def set_iso():
	isoSet = subprocess.Popen(["gphoto2", "--set-config", "iso=0"], stdout=subprocess.PIPE)
	print isoSet.communicate()[0] + "ISO set"

#the shutter speed as well operates using the array position, thus the value for
#this exposure setting is 
def set_shutter_speed():
	ssSet = subprocess.Popen(["gphoto2", "--set-config", "shutterspeed=41"], stdout=subprocess.PIPE)
	print ssSet.communicate()[0] + "Shutter Speed Set"

#simple function for triggering the capture mode of the camera
def Capture():
	cap = subprocess.Popen(["gphoto2", "--capture-image-and-download"], stdout=subprocess.PIPE)
	print cap.communicate()[0] + "TRIIGGGEERRRR"


if(response == "ACK"):
	print("acknowledgement received")
	detect_cam()
	set_iso()
	set_shutter_speed()
	Capture()	
