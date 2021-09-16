import pyautogui, sys
import cv2
from time import sleep


##########Functions################
def clickleft():    #simulates a left click
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    
def findandclick(imgpath):      #find and clicks on the image provided in imgpath
    imgLocation = pyautogui.locateOnScreen(imgpath,confidence=0.8)
    while imgLocation == None:
        imgLocation = pyautogui.locateOnScreen(imgpath,confidence=0.8)
    imgLocation = pyautogui.center(imgLocation)
    pyautogui.moveTo(imgLocation.x,imgLocation.y)
    print("Found it")
    sleep(0.3)
    clickleft()
def waitforserver(image):
    while pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8) != None:
        pass
        

###################################


images = ["./res/1000g.jpg","./res/1000g2.PNG","./res/claim.PNG","./res/waitingforserver.jpg"]

print("Ctrl-C to exit\n")
while True:
    try:
        qunatity = int(input("Amount of packs that will be bought with gold "))
        break
    except KeyboardInterrupt:
        print("Aborted")
        sys.exit()
    except:
        print("Wrong input")

for i in range(qunatity):
     print("Buying "+str(i+1)+". pack")
     print("Looking for 1000g button...")
     findandclick(images[0])     
     print("Looking for 1000g button...")                       
     findandclick(images[1])
     sleep(1)
     waitforserver(images[3])
     sleep(1)
     print("Looking for claim button...")
     findandclick(images[2])
     waitforserver(images[3])
     sleep(2)
print("Done!")
