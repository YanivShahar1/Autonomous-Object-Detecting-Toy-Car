from flask import Blueprint, jsonify, send_file
import os
# from car_AI.constants import *

import constants
image_routes = Blueprint('image_routes', __name__)

album_image_index = 0



# ANSI Colors
ANSI_COLOR_RED = '\033[91m'
ANSI_COLOR_GREEN = '\033[92m'
ANSI_COLOR_BLUE = '\033[94m'
ANSI_COLOR_RESET = '\033[0m' 


def get_all_img(folder_path):
    """
    Retrieve a list of image file paths from a specified folder.

    Args:
        folder_path (str): The path to the folder containing image files.
        n (int): The maximum number of image paths to retrieve.

    Returns:
        list: A list of the last n images paths.
    """
    image_paths = []

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Get a list of image files in the folder
        image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        # Define a sorting key function
        def get_image_index(filename):
            """
            Extract the index from the filename (assuming "image_index.ext" format)
            """
            parts = filename.split('_')

            if len(parts) != 2:
                raise ValueError(f"Invalid filename format. Expected 'image_index.ext', but got '{filename}'")

            index_str = parts[1]
            index_str_without_extension = os.path.splitext(index_str)[0]
            
            if not index_str_without_extension.isdigit():
                raise ValueError(f"Invalid filename format. Expected 'image_index.ext', but got '{filename}'")

            return int(index_str_without_extension)


            
        # Sort image files by index in descending order
        sorted_image_files = sorted(image_files, key=get_image_index, reverse=True)
        
        # Create a list of image paths, limited by max_count
        image_paths = [os.path.join(folder_path, file) for file in sorted_image_files]


    return image_paths

def get_curr_run_folder(image_type = "detection"):
    """
    Get the current run folder for a specific image type.

    This function constructs the path to the current run folder for a given image type. It uses the last
    run index obtained from the `get_last_run_index()` function and constructs the path by appending the
    image type and run index to the appropriate directory.

    Args:
        image_type (str): The type of images for which to get the run folder (e.g., 'detection', 'original').

    Returns:
        str: The absolute path to the current run folder for the specified image type.
    """
    def get_curr_run_index():
        try:
            # Get the file path by navigating up two levels from the current directory
            with open( constants.RUN_INDEX_PATH_FILE, 'r') as file:
                run_index = int(file.read())
            return run_index
        except FileNotFoundError:
            print("File not found")
            return 0
    
    runIndex = get_curr_run_index()  
    # Construct the path to the current run folder
    if image_type == "detection":
        img_dir = constants.OUTPUT_DETECTION_IMAGES_DIR
    else:
        img_dir = constants.OUTPUT_ORIGINAL_IMAGES_DIR

    run_folder = os.path.join(img_dir, f"run{runIndex}" )
                              
    return run_folder

def get_last_image_path(image_type):
    run_folder = get_curr_run_folder(image_type)
    image_paths = get_all_img(run_folder)
    # print(f"\n--\nimage_paths are {image_paths}\n--\n")
    return image_paths[0] if image_paths else None

@image_routes.route('/images/detection/last')
def get_last_detection_image():
    image_path = get_last_image_path(image_type="detection")
    if image_path:
        return send_file(image_path, mimetype='image/jpeg')  # Change mimetype according to image type
    
    return jsonify(image_path=None)

@image_routes.route('/images/original/last')
def get_last_original_image():
    image_path = get_last_image_path(image_type="original")
    # print(f"\n--\nimage path is {image_path}\n--\n")
    if image_path:
        return send_file(image_path, mimetype='image/jpeg')  # Change mimetype according to image type
    
    return jsonify(image_path=None)

def get_image():
    global album_image_index

    run_folder = get_curr_run_folder(image_type = "detection")
    image_paths = get_all_img(run_folder)

    if album_image_index < len(image_paths):
        return image_paths[album_image_index] if image_paths else None
    else:
        album_image_index = len(image_paths) - 1
        return image_paths[album_image_index] if image_paths else None

@image_routes.route('/images/album/prev')
def get_prev_image():
    global album_image_index
    if album_image_index > 0:
        album_image_index -= 1
    print(f"{ANSI_COLOR_GREEN}album_image_index =  {album_image_index} {ANSI_COLOR_RESET}")
    image_path = get_image()
    if image_path:
        return send_file(image_path, mimetype='image/jpeg') 
    
    return jsonify(image_path=None)

@image_routes.route('/images/album/next')
def get_next_image():
    global album_image_index
    album_image_index += 1
    image_path = get_image()    
    print(f"{ANSI_COLOR_GREEN}album_image_index =  {album_image_index} {ANSI_COLOR_RESET}")
    if image_path:
        return send_file(image_path, mimetype='image/jpeg') 
    
    return jsonify(image_path=None)
