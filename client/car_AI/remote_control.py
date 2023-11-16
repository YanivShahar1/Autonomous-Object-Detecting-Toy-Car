import urllib.request
import time
from constants import *
import requests

def set_resolution(resolution_index: int = 1, show_resolution_options: bool = False):
    try:
        if show_resolution_options:
            available_resolutions = {
                10: "UXGA (1600x1200)",
                9: "SXGA (1280x1024)",
                8: "XGA (1024x768)",
                7: "SVGA (800x600)",
                6: "VGA (640x480)",
                5: "CIF (400x296)",
                4: "QVGA (320x240)",
                3: "HQVGA (240x176)",
                0: "QQVGA (160x120)"
            }
            print("Available resolutions:")
            for index, resolution in available_resolutions.items():
                print(f"{index}: {resolution}")
        
        valid_resolution_indices = [10, 9, 8, 7, 6, 5, 4, 3, 0]
        if resolution_index in valid_resolution_indices:
            requests.get(f"{CAR_ESP_32_URI}/control?var=framesize&val={resolution_index}")
            print(f"resulution is {available_resolutions.get(resolution_index)}")
        else:
            print("Invalid resolution index selected.")
    except requests.RequestException:
        print("An error occurred while trying to set the resolution.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def move_forward():
    try:
        urllib.request.urlopen(FORWARD_URI,timeout=2)
    except urllib.error.URLError as e:
        print(f"URLError occurred while sending the 'go forward' command:\n {e}")

def move_backward():
    try:
        urllib.request.urlopen(BACKWARD_URI,timeout=2)
    except urllib.error.URLError as e:
        print(f"URLError occurred while sending the 'go back' command:\n {e}")

def stop():
    try:
        urllib.request.urlopen(f"{STOP_URI}", timeout=2)
    except urllib.error.URLError as e:
        print(f"URL error occurred while stopping the car:\n {e}")
 
def set_speed(speed):
    if speed < 30 or speed > 100:
        raise ValueError("Speed value must be in the range 30 to 100. or 0 to stop the car")
    try:
        urllib.request.urlopen(f"{SET_SPEED_URI}?Speed={speed}" ,timeout=2)
        print(f"set car speed to {speed} successfully")
    except urllib.error.URLError as e:
        print(f"URLError occurred while setting the speed to {speed}: {e}")
    except Exception as e:
     print(f"An unexpected error occurred while setting the speed to {speed} {e}\n")


def capture_img():
    try:
        response = urllib.request.urlopen(CAPTURE_URI,timeout=5)
        return response
    except Exception as e:
        raise Exception(f"An unexpected error occurred while capturing image: {e}\n")



def server_available():
    """
    Check if the car esp32 server is available.

    Sends a request to the car server to check its availability.

    Returns:
        bool: True if the car server is available, False otherwise.
    """
    try:
        urllib.request.urlopen(CAR_ESP_32_URI,timeout=3)
        return True
    except Exception as e:
        return False


def lights(turn_on):
    #the car server need to implement this uri
    if turn_on:
        try:
            urllib.request.urlopen(f"{LIGHTS_URI}?On={True}", timeout=2)
        except urllib.error.URLError as e:
            print(f"URLError occurred while turning the lights on: {e}")
    else:
        try:
            urllib.request.urlopen(f"{LIGHTS_URI}?On={False}", timeout=2)
        except urllib.error.URLError as e:
            print(f"URLError occurred while turning the lights off: {e}")
