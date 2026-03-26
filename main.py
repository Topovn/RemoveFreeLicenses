import pyautogui
import pytesseract
import time
import keyboard
import cv2
import numpy as np
import os

keyboard.add_hotkey('esc', lambda: os._exit(0))

# Default Tesseract installation location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_text_in_radius(target_word, radius=800, action='click'):
    """Scans an area, applies high-contrast filter, and clicks text."""
    mouse_x, mouse_y = pyautogui.position()
    
    box_x = max(0, mouse_x - radius)
    box_y = max(0, mouse_y - radius)
    
    screenshot = pyautogui.screenshot(region=(box_x, box_y, radius*2, radius*2))
      
    # This turns dark grey backgrounds black, and light text pure white
    cv_img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    _, thresh_img = cv2.threshold(cv_img, 120, 255, cv2.THRESH_BINARY_INV)
    
    data = pytesseract.image_to_data(thresh_img, output_type=pytesseract.Output.DICT)
    
    for i, text in enumerate(data['text']):
        if target_word.lower() in text.lower():
            click_x = box_x + data['left'][i] + (data['width'][i] // 2)
            click_y = box_y + data['top'][i] + (data['height'][i] // 2)
            
            if action == 'click':
                pyautogui.leftClick(click_x, click_y)
            elif action == 'hover':
                pyautogui.moveTo(click_x, click_y)
            return True
            
    return False

def wait_and_find_text(target_word, timeout=3.0, radius=800, action='click'):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if find_text_in_radius(target_word, radius, action):
            return True
            
        time.sleep(0.2) 
        
    return False

def main():
    print("Waiting 5 seconds, hover over a steam game in grid view to begin")
    time.sleep(5)
    
    point_a = pyautogui.position()
    #print(f"Initial position locked at: {point_a}")

    # Change this if you want
    total_loop = 50

    for i in range(total_loop):
        print(f"Cycle {i+1}/{total_loop}")
        pyautogui.moveTo(point_a)
        pyautogui.rightClick()
        time.sleep(0.2)
        
        if not wait_and_find_text("Manage", action='hover'):
            #print("Failed to find 'Manage'. Retrying next cycle.")
            continue
    
        if not wait_and_find_text("account", action='click'):
            #print("Failed to find 'Remove from account'. Retrying next cycle.")
            continue
        
        if not wait_and_find_text("Would", action="click"):
             #print("Failed to find 'Would'. Retrying next cycle.")
             continue
        pyautogui.move(500,110)
        pyautogui.click()
            
        pyautogui.moveTo(point_a)
        time.sleep(2)

    print("Task complete.")

if __name__ == "__main__":
    main()