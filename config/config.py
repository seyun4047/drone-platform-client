"""Define project constants"""

# Tesseract Path
# MAC OS!!!
TESSERACT_PATH = '/opt/homebrew/bin/tesseract'
# WINDOWS!!!
# TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# DEFINE ROI TYPE
ROI_TYPES = {
    'SPEED': 0,
    'PERSON': 1,
    'LONGITUDE': 2,
    'LATITUDE': 3,
    # 'CUSTOM': 4
}

# ROI NAME
ROI_NAMES = {
    0: 'Speed Detect',
    1: 'Person Detect',
    2: 'Longitude Detect',
    3: 'Latitude Detect',
    # 4: 'CUSTOM DETECT'
}

# DETECT INTERVAL
DEFAULT_INTERVAL = 1.0

# MIN INTERVAL
MIN_INTERVAL = 0.05

# ROI OVERLAY COLOR (R, G, B)
ROI_COLORS = {
    0: (255, 0, 0),     # RED - SPEED
    1: (0, 255, 0),     # GREEN - PERSON
    2: (0, 0, 255),     # BLUE - LONGITUDE
    3: (255, 255, 0),   # YELLOW - PERSON
    # 4: (255, 0, 255)    # MAGENTA - CUSTOM
}