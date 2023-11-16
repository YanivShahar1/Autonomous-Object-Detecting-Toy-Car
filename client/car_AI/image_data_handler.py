import os
import csv
import cv2
import constants 

def get_image_with_detections(img,classesInImg, bboxes, colors, confidence):
    """
    Annotate the input image with bounding boxes and class labels.

    This function draws bounding boxes around detected objects in the image 
    and labels each box with the class name and confidence score.

    Parameters:
    - img (numpy.ndarray): The input image on which detections will be drawn.
    - classesInImg (list): List of class names corresponding to each bounding box.
    - bboxes (list): List of bounding boxes, where each box is represented as 
                     [x_min, y_min, x_max, y_max].
    - colors (list): List of colors for each bounding box. Each color is represented 
                     as a tuple (R, G, B).
    - confidence (list): List of confidence scores for each detection.

    Returns:
    - numpy.ndarray: The annotated image.
    """
    for i,bbox in enumerate(bboxes):
        #draw rectangle
        x_min , y_min, x_max, y_max = bbox[0], bbox[1], bbox[2], bbox[3]
        cv2.rectangle(img, (x_min, y_min),
                    (x_max, y_max), colors[i], 2)
        # Add class label and confidence
        label = f'{classesInImg[i][0]}: {confidence[i]:.2f}'
        # print(f"label : {label}")

        # Put the text on top of the rectangle
        # cv2.putText(img, 
        #             label, 
        #             (max(0, min(img.shape[1] - 50, x_min - 50)), max(20, y_min - 10)), 
        #             cv2.FONT_HERSHEY_SIMPLEX, 
        #             1, 
        #             colors[i], 
        #             1)
        
        # cv2.putText(img, label, (max(0, min(img.shape[1] - 50, x_min - 50)), max(20, y_min - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[i], 2)
        cv2.putText(img, label, (int(x_min) - 50, int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[i], 2)
    return img

def save_detection_img(img, obj_in_img : list, bboxes : list, colors : list, confidence : list, imgCounter, runIndex ):
    img = get_image_with_detections(img, obj_in_img, bboxes, colors, confidence)
    output_detection_path = os.path.join(constants.OUTPUT_DETECTION_IMAGES_DIR,f'run{runIndex}', f'image_{imgCounter}.jpg')
    cv2.imwrite(output_detection_path, img)
    return img

def extract_detection_info(results):
    """
    Extract and filter detection data from results.

    Parameters:
    - results: Detection results, typically from a YOLO-based detector.

    Returns:
    - classesList (list): Detected object names and areas.
    - bboxesList (list): Bounding boxes [x_min, y_min, x_max, y_max].
    - colorsList (list): Colors for each detected object.
    - confidenceList (list): Confidence scores for detections.
    """
    df = results.pandas().xyxy[0] 

    bboxesList = []
    classesList = []
    colorsList = []
    confidenceList = []

    # Iterate over each detection in the dataframe
    for _, row in df.iterrows():
        obj_index = int(row['class'])
        obj_name = constants.ALL_OBJECTS[obj_index]["name"]
        # Filter detections based on a predefined threshold
        if row['confidence'] > constants.ALL_OBJECTS[obj_index]["threshold"]:
            bboxesList.append([int(row['xmin']), int(row['ymin']),
                                int(row['xmax']), int(row['ymax'])])
            
            area = (int(row['xmax']) - int(row['xmin'])) * (int(row['ymax']) -  int(row['ymin']))
            # classesList.append(obj_name)
            classesList.append((obj_name,area))
            colorsList.append(constants.ALL_OBJECTS[obj_index]["color"])
            confidenceList.append(row['confidence'])
            
    return classesList, bboxesList, colorsList, confidenceList

def save_original_and_detection_img(img ,  classesInImg : list, bboxes : list, colors : list, confidence : list,imgCounter, currClientRunIndex): 
    save_original_img(img,imgCounter,currClientRunIndex)
    save_detection_img(img,classesInImg,bboxes,colors,confidence,imgCounter, currClientRunIndex  )

def save_original_img(img, imgCounter, run_index):
    output_original_path = os.path.join(constants.OUTPUT_ORIGINAL_IMAGES_DIR,f'run{run_index}', f'image_{imgCounter}.jpg')
    cv2.imwrite(output_original_path, img)

def print_results(classes, confidence,model_elapsed_time):
    print("detectded objects: \n")
    for i in range (len(classes)):
            print(f"{constants.ANSI_COLOR_BLUE} {classes[i]} : {confidence[i]:.2f} {constants.ANSI_COLOR_RESET}")
    print(f"\n\nModel time: {model_elapsed_time:.3f} sec")
    print("\n---------------------------------------------------\n")


def roi(img):
    """
    Returns the Region of Interest (ROI) of the image

    Args:
    - img (numpy.ndarray): The input image.

    Returns:
    - numpy.ndarray: The cropped image representing the region of interest.
    """
    height, width, _ = img.shape
    return img[int(height/6):, :]

def get_client_run_index():
    """
    Retrieve the index for the next run folder.

    This function checks if a file containing the last run index exists. If it does, 
    it reads the index, increments it by one, and returns it. If the file doesn't exist,
    it means this is the first run, so it returns an index of 1.

    Returns:
    - int: The index for the next run folder.
    """
    if os.path.exists(constants.RUN_INDEX_PATH_FILE):
        with open(constants.RUN_INDEX_PATH_FILE, 'r') as file:
            run_index = int(file.read()) + 1
    else:
        run_index = 1 #first
    return run_index

def create_run_folder_for_images():
    run_index = get_client_run_index()
    original_images_folder = f"{constants.OUTPUT_ORIGINAL_IMAGES_DIR}\\run{run_index}"
    if not os.path.exists(original_images_folder):
        os.makedirs(original_images_folder)

    detections_folder = f"{constants.OUTPUT_DETECTION_IMAGES_DIR}\\run{run_index}"  
    if not os.path.exists(detections_folder):
        os.makedirs(detections_folder) 

    return run_index

def update_run_index(run_index):
    with open(constants.RUN_INDEX_PATH_FILE, 'w') as file:
        file.write(str(run_index))
