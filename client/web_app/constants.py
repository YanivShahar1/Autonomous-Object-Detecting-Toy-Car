import os 

# Data
OUTPUT_DETECTION_IMAGES_DIR = os.path.join(os.getcwd(), "data", "images", "detection")
OUTPUT_ORIGINAL_IMAGES_DIR = os.path.join(os.getcwd(), "data", "images","original")
OUTPUT_LANE_IMAGES_DIR = os.path.join(os.getcwd(), "data", "images","lane")
NAVIGATE_DATA_IMG_DIR = os.path.join(os.getcwd(), "data", "navigateData","img")
NAVIGATE_DATA_DIRECTION_DIR = os.path.join(os.getcwd(), "data", "navigateData","directions")
RUN_INDEX_PATH_FILE = os.path.join(os.getcwd(), "data", "last_run_index.txt")
TURNS_DATA_PATH_FILE = os.path.join(os.getcwd(), "data", "turns_data.txt")
OUTPUT_TEST_PATH = os.path.join(os.getcwd(), "data", "test", "output")
TEST_IMAGES_PATH = os.path.join(os.getcwd(), "data", "test", "images")
TEST_LABELS_PATH = os.path.join(os.getcwd(), "data", "test", "labels")