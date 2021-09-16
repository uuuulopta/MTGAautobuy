### What is this

------------


Because developers of [MTGA](https://magic.wizards.com/en/mtgarena "MTGA") are forcing us to buy packs one by one I created a script that lets you input the amount of packs you want to buy and it does it for you!

### How to run

------------


Make sure you at least have [Python](https://www.python.org/ "Python") 3.7.x installed.

You can install dependencies with pipenv or by installing them individually listed below.
You can install pipenv with 

`pip install pipenv` in the command line

1. Download files via clicking code -> download as zip and extract it or clone it via git. 
 
2. Run cmd as and Administrator *(required to allow mouse clicks)* and navigate to the folder. 

4. Make sure MTGA is in fullscren and the resolution is 1366x768 (it will probably work in others but this one is for sure)

5. In MTGA be in the pack section of the pack you want to buy. It should look like [this](https://i.imgur.com/jcFm9Lg.png "this"). For each different pack you have to select the pack section and run the script again.

6. Install dependencies with `pipenv install` or install them individually with commands listed below

8. Run with `pipenv run python main.py` or just without pinpenv `python main.py` 

9. Type the number of packs you want to buy

10. Alt tab to MTGA **DO NOT MOVE YOUR MOUSE**
### Dependencies
------------
- **pyautogui** install it with `pip install pyautogui`

- **cv2** install it with `pip install opencv-python` *(required by pyautogui)*
