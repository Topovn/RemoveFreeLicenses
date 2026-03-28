import pyautogui
import time
import os
from pynput import keyboard
from pynput.keyboard import Key

# Change this if u want the script to run shorter/longer
totalLoop = 500

# --------------------------------
SCALE = 2.0     # Mac Retina screen
startTime = time.time()

def printElapsedTime(message: str = "Task complete"):
    elapsed = time.time() - startTime
    mins = int(elapsed // 60)
    secs = int(round(elapsed % 60))
    print(message)
    print(f"Ran for {mins} minutes {secs} seconds")
    
def stopScript():
    printElapsedTime("Stopped by user")
    os._exit(0)

def onPress(key):
    if key == Key.esc:
        stopScript()

listener = keyboard.Listener(on_press=onPress)
listener.daemon = True
listener.start()

time.sleep(1)

initPoint = None

def resetPostion():
    pyautogui.moveTo(initPoint)
    pyautogui.moveRel(0, -10) 
    pyautogui.click()
    pyautogui.moveTo(initPoint)
    time.sleep(0.2)

def wait_and_act(imagePath, timeout=3.0, action='click',conf=0.9):
    startTimeLoop = time.time()
    
    while time.time() - startTimeLoop < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(imagePath, confidence=conf)
            
            if location:
                x = location.x / SCALE
                y = location.y / SCALE

                if action == 'click':
                    pyautogui.leftClick(x,y)
                elif action == 'hover':
                    pyautogui.moveTo(x,y)
                return True
        except pyautogui.ImageNotFoundException:
            pass 
            
        time.sleep(0.2)
    return False

def main():
    print("Waiting for 5 seconds, hover over a steam game in grid view to begin")
    time.sleep(5)

    global initPoint
    initPoint = pyautogui.position()
    scrollDown = 0
    hideGame = 0

    try:
        for _ in range(totalLoop):
            pyautogui.moveTo(initPoint)
            pyautogui.rightClick()
            time.sleep(0.2)
            
            if not wait_and_act('img/manageMac.png', action='hover'):
                # print("Failed to find 'Manage'")
                scrollDown += 1
                if scrollDown >= 2:
                    if scrollDown >= 5:
                        print("Something went wrong, maybe SteamWebService isnt responding. Stopping the script")
                        break
                    pyautogui.scroll(-30)
                    scrollDown = 0
                resetPostion()
                continue

            if not wait_and_act('img/removeMac.png', action='click'):
                # print("Failed to find 'Remove from account'")
                hideGame += 1
                if hideGame >= 2:
                    # print("Could not remove game, now hiding from view")
                    if wait_and_act('img/hideMac.png', action='click'):
                        hideGame = 0
                        time.sleep(1)
                        continue
                resetPostion()
                continue

            hideGame = 0
            
            if not wait_and_act('img/confirmMac.png', action="click"):
                # print("Failed to find 'Remove'")
                resetPostion()
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        stopScript()

    printElapsedTime()


if __name__ == "__main__":
    main()