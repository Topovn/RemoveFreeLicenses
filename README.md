# Steam Free License Remover

Quick script I wrote that uses OCR to remove free licenses from Steam library
Yes I know you used [SteamDB Freepackages](https://steamdb.info/freepackages/https://steamdb.info/freepackages/)

Press ESC key to exit while script is running

## Prerequisites

1. Create a dynamic collection with "Free to Play" store tag. View said collection in Grid view

2. Download the Tesseract OCR from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

3. Install the libraries via pip:
```bash
pip install pyautogui pytesseract keyboard opencv-python numpy
```

4. Run the script 
```python
python main.py
```
and look at the log for further instruction

## Disclaimer
I take no responsibility, it works on my machine (sometimes it breaks just restart)
