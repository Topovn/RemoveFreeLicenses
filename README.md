# Steam Free Licenses Remover

Quick script I wrote that uses OCR to remove free licenses from Steam library

Yes I know you used [SteamDB's Freepackages](https://steamdb.info/freepackages/)

also, press ESC key to exit while the script is running

## Prerequisites

1. Create a dynamic collection with "Free to Play" store tag. View said collection in Grid view

2. Set up environment
```bash
git clone
cd
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
pip install pyautogui keyboard opencv-python
```

3. Modify totalLoop if you want and run the script 
```python
python main.py  # For Windows
or
python mac.py   # For Mac
```
and look at the log for further instruction

## Showcase

https://github.com/user-attachments/assets/ec3b052f-ba82-47c3-b04f-94b40446fddb

## Disclaimer
I take no responsibility, it works on my machine
