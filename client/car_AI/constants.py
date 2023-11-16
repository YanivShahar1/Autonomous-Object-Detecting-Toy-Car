import os

INITIAL_SPEED = 35
CROSSWALK_SPEED = 35
LIMIT_100_SPEED = 65
LIMIT_50_SPEED = 50

import os 

# Data
OUTPUT_DETECTION_IMAGES_DIR = os.path.join(os.getcwd(), "data", "images", "detection")
OUTPUT_ORIGINAL_IMAGES_DIR = os.path.join(os.getcwd(), "data", "images","original")
RUN_INDEX_PATH_FILE = os.path.join(os.getcwd(), "data", "last_run_index.txt")
OUTPUT_TEST_PATH = os.path.join(os.getcwd(), "data", "test", "output")
TEST_IMAGES_PATH = os.path.join(os.getcwd(), "data", "test", "images")
TEST_LABELS_PATH = os.path.join(os.getcwd(), "data", "test", "labels")
# Car control URIs
# CAR_ESP_32_URI = "http://192.168.86.9"
# CAR_ESP_32_URI = "http://192.168.238.9"
# CAR_ESP_32_URI = "http://192.168.240.9"
# CAR_ESP_32_URI = "http://192.168.110.9"
CAR_ESP_32_URI = "http://192.168.148.9"
PORT = 80

FORWARD_URI = f"{CAR_ESP_32_URI}:{PORT}/forward"
BACKWARD_URI = f"{CAR_ESP_32_URI}:{PORT}/backward"
RIGHT_URI = f"{CAR_ESP_32_URI}:{PORT}/right" 
LEFT_URI = f"{CAR_ESP_32_URI}:{PORT}/left"
SET_SPEED_URI = f"{CAR_ESP_32_URI}:{PORT}/set_speed"
CAPTURE_URI = f"{CAR_ESP_32_URI}:{PORT}/capture"
LIGHTS_URI = f"{CAR_ESP_32_URI}:{PORT}/lights" # TO DO -> implement this endpoint on the car server side
STOP_URI = f"{CAR_ESP_32_URI}:{PORT}/stop"


# Object names
STOP_SIGN = 'Stop'
SPEED_LIMIT_50_SIGN = '50'
PEDESTRIAN = 'Pedestrian'
KEEP_RIGHT = 'KeepRight'
CROSSWALK_SIGN = 'CrossWalk'
SPEED_LIMIT_100_SIGN = '100'



# ANSI Colors
ANSI_COLOR_RED = '\033[91m'
ANSI_COLOR_GREEN = '\033[92m'
ANSI_COLOR_BLUE = '\033[94m'
ANSI_COLOR_RESET = '\033[0m' 


# List of All Objects with attributes
ALL_OBJECTS = [     {"name" : STOP_SIGN       ,  "threshold" : 0.75   ,   "color" : (0, 0, 255) },
                    {"name" : SPEED_LIMIT_50_SIGN  ,  "threshold" : 0.84    ,  "color" : (0, 255, 0) },
                    {"name" : PEDESTRIAN      ,  "threshold" : 0.75    ,  "color" : (255, 0, 0) },
                    {"name" : KEEP_RIGHT      ,  "threshold" : 0.9   ,  "color" : (255, 100, 0) },
                    {"name" : CROSSWALK_SIGN       ,  "threshold" : 0.8    ,  "color" : (180, 100, 10) },
                    {"name" : SPEED_LIMIT_100_SIGN ,  "threshold" : 0.83    ,  "color" : (50, 100, 60) }   ]

# objects area in meters
OBJECTS_AREA = {SPEED_LIMIT_50_SIGN: 0.36, 
                SPEED_LIMIT_100_SIGN: 0.49,
                CROSSWALK_SIGN: 0.45,
                PEDESTRIAN: 0.30,
                STOP_SIGN:0.33,
                KEEP_RIGHT: 0.25
                }