import pyautogui
import time
import keyboard
import os

keyboard.add_hotkey('esc', lambda: os._exit(0))

def wait_and_act(imagePath, timeout=3.0, action='click',conf=0.9):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(imagePath, confidence=conf)
            
            if location:
                if action == 'click':
                    pyautogui.leftClick(location)
                elif action == 'hover':
                    pyautogui.moveTo(location)
                return True
        except pyautogui.ImageNotFoundException:
            pass 
            
        time.sleep(0.2)
    return False

def main():
    print("Waiting 5 seconds, hover over a steam game in grid view to begin")
    time.sleep(5)
    
    initPoint = pyautogui.position()
    #print(f"Initial position locked at: {initPoint}")

    # Change this if you want
    totalLoop = 200

    scrollDown = 0
    hideGame = 0
    for _ in range(totalLoop):
        #print(f"Cycle {_+1}/{totalLoop}")
        pyautogui.moveTo(initPoint)
        pyautogui.rightClick()
        time.sleep(0.2)
        
        if not wait_and_act('img/manage.png', action='hover'):
            # print("Failed to find 'Manage'")
            scrollDown += 1
            if scrollDown >= 2:
                if scrollDown >= 10:
                    print("Something went wrong, maybe SteamWebService isnt responding. Stopping the script")
                    break
                pyautogui.scroll(-30)
                scrollDown = 0
            pyautogui.press('esc')
            time.sleep(1)
            continue
    
        if not wait_and_act('img/remove.png', action='click'):
            # print("Failed to find 'Remove from account'")
            hideGame += 1
            if hideGame >= 2:
                # print("Could not remove game, now hiding from view")
                if wait_and_act('img/hide.png', action='click'):
                    hideGame = 0
                    time.sleep(1)
                    continue
            pyautogui.press('esc')
            time.sleep(0.5)
            continue

        hideGame = 0
        
        if not wait_and_act('img/confirm.png', action="click"):
            #  print("Failed to find 'Remove'")
             pyautogui.press('esc')
             time.sleep(1)
        
        time.sleep(2)

    print("Task complete.")

if __name__ == "__main__":
    main()