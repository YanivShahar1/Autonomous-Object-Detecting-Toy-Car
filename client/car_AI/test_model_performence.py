import sys
sys.path.append(r"C:\Users\Yaniv\Desktop\RoboWheel\carAsServer-try\client")
import cv2 as cv
import numpy as np
import time
import remote_control as car
import image_data_handler as img_handler
from hubconf import custom as load_custom_model
from car_AI.constants import *
from obj_handlers import *
import os

LABELS = {STOP_SIGN:0, SPEED_LIMIT_50_SIGN:1, PEDESTRIAN:2, KEEP_RIGHT:3, CROSSWALK_SIGN:4, SPEED_LIMIT_100_SIGN:5}
# Load model
# model_to_test = "car_AI/yolov7_RoboWheel_v7.pt"

# so far the best models: 
# v14 75.37% accuracy, 394 miliseconds per image
# v20 82.84% accuracy, 355 miliseconds per image
model_to_test = "car_AI/weights/yolov7tiny_RoboWheel_v20.pt"

detection_model = load_custom_model(path_or_model=model_to_test)

def find_labels(image_path):
    # Assuming label file has the same name as the image file with a .txt extension
    label_filename = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
    label_path = os.path.join(TEST_LABELS_PATH, label_filename)
    
    # Read the label file and extract labels
    labels = []
    try:
        with open(label_path, "r") as label_file:
            for line in label_file:
                class_index = int(line.strip()[0])  # Assuming label is a single integer on each line, first in the row
                labels.append(class_index)
    except FileNotFoundError:
        print(f"{ANSI_COLOR_RED}Label file not found for {image_path}")
    
    return labels


def compare(labels, detected_objects):
    # Compare the detected objects with the ground truth labels
    # and return 1 if all labels are detected, otherwise 0.
    detected_labels = []
    for obj, area in detected_objects:
        detected_labels.append(LABELS[obj])

    # print(f"detected_labels = {detected_labels}")
    if set(labels) == set(detected_labels):
        return 1
    else:
        return 0
import os
import cv2

def show_images_with_classes(image_folder, label_folder, classes_to_show):
    # Iterate through label files
    for label_filename in os.listdir(label_folder):
        if label_filename.endswith(".txt"):
            label_file_path = os.path.join(label_folder, label_filename)

            # Read the content of the label file
            with open(label_file_path, "r") as label_file:
                lines = label_file.readlines()

            # Check if any of the specified classes is present in any line
            if any(line.split()[0] in map(str, classes_to_show) for line in lines):
                # Determine the corresponding image file path
                image_filename = os.path.splitext(label_filename)[0] + ".jpg"
                image_path = os.path.join(image_folder, image_filename)

                # Check if the image file exists and display it
                if os.path.exists(image_path):
                    image = cv2.imread(image_path)
                    cv2.imshow(f"{label_filename}", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

def detect(img):
    """
    Detects objects in an input image using the YOLO v7 object detection model.

    Returns:
    - detection_time
    - img_with_detections
    - objects_in_img (list): List of detected object labels.
    """
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # img_resized = cv.resize(rgb_img, (416,320))
    
    # Run the object detection model
    detect_start_time = time.time()
    model_results = detection_model(rgb_img) 
    objects_in_img, bboxes, colors, confidence = img_handler.extract_detection_info(model_results)
    print(f"objects in image : {objects_in_img}")
    detection_time = time.time() - detect_start_time
    img_with_detections = img_handler.get_image_with_detections(img, objects_in_img, bboxes, colors, confidence)

    
    return detection_time , img_with_detections, objects_in_img

def run_test():
    total_images = 0
    total_correct = 0
    total_detections_time = 0 # ms
    for image_filename in os.listdir(TEST_IMAGES_PATH):
        if image_filename.endswith(".jpg"):
            print(f"testing : {image_filename}")
            image_path = os.path.join(TEST_IMAGES_PATH, image_filename)
            
            # Find labels for the current image
            labels = find_labels(image_path)
            
            # Detect objects in the image
            img = cv.imread(image_path)
            detection_time, img_with_detections, objects_in_img = detect(img)
            total_detections_time += detection_time
            output_detection_path = os.path.join(OUTPUT_TEST_PATH, f'{image_filename}')
            cv.imwrite(filename=output_detection_path, img= img_with_detections)
            # print(f"labels: {labels}\n detected objects: {objects_in_img}")
            # Compare detected objects with labels
            score = compare(labels, objects_in_img)
            if score == 1:
                print(f"{ANSI_COLOR_GREEN} passed {ANSI_COLOR_RESET}")
            else:
                print(f"{ANSI_COLOR_RED} failed{ANSI_COLOR_RESET}")

                
            
            total_images += 1
            total_correct += score

    accuracy = total_correct / total_images if total_images > 0 else 0

    print(f"{ANSI_COLOR_GREEN} Test results for mdoel {model_to_test} :\n")
    print(f"Total images tested: {total_images}")
    print(f"Correctly detected images: {total_correct}")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Average detection time per image: {(total_detections_time/total_images):.3f} sec{ANSI_COLOR_RESET} ")


import time
if __name__ == '__main__':
    # Usage example:
    image_folder = r"C:\Users\Yaniv\Desktop\RoboWheel\images-new data\all new images"
    label_folder = r"C:\Users\Yaniv\Desktop\RoboWheel\images-new data\all labels"
    classes_to_show = [1,5]  # List of classes to show
    # show_images_with_classes(image_folder, label_folder, classes_to_show)
    run_test()
   

    
