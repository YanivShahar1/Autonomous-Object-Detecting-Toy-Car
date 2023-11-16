import sys
import cv2 as cv
import numpy as np
import time
import remote_control as car
import image_data_handler as img_handler
from hubconf import custom as load_custom_model
from constants import *
from obj_handlers import *

# Load trained model
modelPath = "car_AI/weights/yolov7tiny_RoboWheel_v20.pt"
detection_model = load_custom_model(path_or_model=modelPath)

car_speed = INITIAL_SPEED

def drive(max_priority_obj,last_obj_in_image, obj_size,car_speed):
    """
    Drives the car based on the detected object.
    """
    if max_priority_obj == PEDESTRIAN:
        car_speed = pedestrian_handler(obj_size, car_speed)
    elif max_priority_obj == STOP_SIGN and last_obj_in_image != STOP_SIGN:
        car_speed = stop_sign_handler(obj_size, car_speed, sleep_time=3)
    elif max_priority_obj == CROSSWALK_SIGN:
        car_speed =  crosswalk_handler(obj_size, car_speed)
    elif max_priority_obj == KEEP_RIGHT:
        car.turn(direction="right", turn_duration=10)
    elif max_priority_obj == SPEED_LIMIT_50_SIGN:
        car_speed = speed_limit_handler(SPEED_LIMIT_50_SIGN)
    elif max_priority_obj == SPEED_LIMIT_100_SIGN:
        car_speed = speed_limit_handler(SPEED_LIMIT_100_SIGN)
    else:
        car.move_forward()

def wait_for_car_server():
    """
    Wait until the server is available.
    """
    while not car.server_available():
        print(f"car uri : {CAR_ESP_32_URI} is not available yet")
        time.sleep(2)
    
def fetch_img_from_car():
    fetch_start_time = time.time()

    try:
        # Capture the image from the car
        capture_start_time = time.time()
        img_response = car.capture_img()
        capture_time = time.time() - capture_start_time
        print(f"{ANSI_COLOR_GREEN}Time to capture image: {capture_time:.4f} seconds{ANSI_COLOR_RESET}")

        # Read the image data from the response
        read_start_time = time.time()
        img_data = img_response.read()
        print(f"{ANSI_COLOR_GREEN}data size: {len(img_data)} bytes {ANSI_COLOR_RESET}")
        read_time = time.time() - read_start_time
        print(f"{ANSI_COLOR_GREEN}Time to read image data: {read_time:.4f} seconds{ANSI_COLOR_RESET}")

        # Convert the image data into a NumPy array for further processing
        img_np = np.array(bytearray(img_data), dtype=np.uint8)
       
        # Decode the NumPy array to obtain the actual image
        img = cv.imdecode(img_np, -1)

        # Rotate the image 90 degrees clockwise
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        
        total_time = time.time() - fetch_start_time
        print(f"\n{ANSI_COLOR_GREEN}Total time for image fetching and processing: {total_time:.4f} seconds{ANSI_COLOR_RESET}\n")

        return img

    except Exception as e:
        raise Exception(f"{ANSI_COLOR_RED}Error fetching or processing image: {e}{ANSI_COLOR_RESET}")
        
def detect(img, img_counter, save_detection_img = True):
    img = img_handler.roi(img)
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # Run the object detection model
    model_start_time = time.time()
    modelResults = detection_model(rgb_img) 
    objects_in_img, bboxes, colors, confidence = img_handler.extract_detection_info(modelResults)
    # print(f"detection info: {objects_in_img,bboxes,colors,confidence}")
    modelElapsedTime = time.time() - model_start_time
    
    if save_detection_img:
        # TODO: new thread to save the detection image
        img_handler.save_detection_img(img,objects_in_img, bboxes, colors, confidence, img_counter, run_ind)
    
    # img_handler.print_results(objects_in_img, confidence, modelElapsedTime)
    return objects_in_img

def get_max_priority_object(detected_objects : list):
    """
    Returns the object with the highest priority from the list of detected objects.

    Parameters:
    - detected_objects (list): A list of tuples containing detected objects and their areas.

    Returns:
    - str: The object with the maximum priority.
    """
    def get_priority_of_object(obj, obj_size ):
        if obj == PEDESTRIAN and (obj_size > 250):
            return 7
        elif obj == STOP_SIGN and obj_size > 400 :
            return 6
        elif obj == CROSSWALK_SIGN and obj_size > 350 :
            return 5
        elif obj == KEEP_RIGHT and obj_size > 1000:
            return 4
        elif obj == SPEED_LIMIT_50_SIGN and obj_size > 100:
            return 3
        elif obj == SPEED_LIMIT_100_SIGN and obj_size > 100 :
            return 2
        else:
            return -10 #
  
    max_priority = -1
    size = 0
    max_priority_obj = None
    for obj, obj_size in detected_objects:
            obj_priority = get_priority_of_object(obj, obj_size)
            if obj_priority > max_priority:
                max_priority = obj_priority
                size = obj_size
                max_priority_obj = obj
    return max_priority_obj,size

def run():
    wait_for_car_server()
    global car_speed
    last_obj_in_image = "none"
    img_counter = 0
    car.set_speed(INITIAL_SPEED)
    while True:
        start_time = time.time()
        try:
            img = fetch_img_from_car()
            # img_handler.save_original_img(img, img_counter, run_ind) # TODO: new thread for saving the images
           
            objects_in_img = detect(img ,img_counter ,save_detection_img = True)
            max_priority_obj, obj_size = get_max_priority_object(objects_in_img)
            drive(max_priority_obj,last_obj_in_image,obj_size,car_speed )

            last_obj_in_image = last_obj_in_image if max_priority_obj == "none" else max_priority_obj

            img_counter += 1
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
        
        finally:
            elapsed_time = time.time() - start_time
            print(f"elapsed_time = {elapsed_time}")
  
if __name__ == '__main__':
    # Initialize a new directory to store images (both original and detection) for the current execution run.
    run_ind = img_handler.create_run_folder_for_images()
    print(f"Assigned run index: {run_ind}")
    img_handler.update_run_index(run_ind)

    run()


    
