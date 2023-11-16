import os
import shutil
from datetime import datetime
import random


def rename_and_split_images(images_folder_path, destination_folder):
    # Create destination folder if it doesn't exist
    print(images_folder_path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of image files in the source folder sorted by date modified
    image_files = sorted(
        [f for f in os.listdir(images_folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))],
        key=lambda x: os.path.getmtime(os.path.join(images_folder_path, x))
    )
    print(f"image_files = {image_files}")
    # Rename images
    for idx, image_file in enumerate(image_files):
        old_image_path = os.path.join(images_folder_path, image_file)
        new_image_name = f"r6_image_{idx}.jpg"
        new_image_path = os.path.join(images_folder_path, new_image_name)

        # Rename the image file
        print(f"renamed { old_image_path} to {new_image_path}")
        os.rename(old_image_path, new_image_path)

    # Split images into subfolders
    images_per_subfolder = len(image_files) // 5

    for subfolder_idx in range(5):
        subfolder_path = os.path.join(destination_folder, f"subfolder_{subfolder_idx}")
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        for idx in range(subfolder_idx * images_per_subfolder, (subfolder_idx + 1) * images_per_subfolder):
            if idx < len(image_files):
                image_file = f"r6_image_{idx}.jpg"
                image_path = os.path.join(images_folder_path, image_file)
                new_image_path = os.path.join(subfolder_path, image_file)

                # Move the image file to the subfolder
                shutil.move(image_path, new_image_path)

def test_val_split(images_folder_path,labels_folder_path, destination_folder, val_ratio = 0.15, test_ratio = 0.1):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    image_files = sorted(
        [f for f in os.listdir(images_folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))],
        key=lambda x: os.path.getmtime(os.path.join(images_folder_path, x))
    )

    random.shuffle(image_files)

    total_images = len(image_files)
    val_split = int(val_ratio * total_images)
    test_split = int(test_ratio * total_images)

    train_images = image_files[val_split + test_split:]
    val_images = image_files[:val_split]
    test_images = image_files[val_split:val_split + test_split]

    subfolders = ['train', 'val', 'test']
    for subfolder in subfolders:
        subfolder_path = os.path.join(destination_folder, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        # Create sub-subfolders for images and labels
        os.makedirs(os.path.join(subfolder_path, 'images'), exist_ok=True)
        os.makedirs(os.path.join(subfolder_path, 'labels'), exist_ok=True)

    move_images(train_images, images_folder_path, os.path.join(destination_folder, 'train', 'images'))
    move_images(val_images, images_folder_path, os.path.join(destination_folder, 'val', 'images'))
    move_images(test_images, images_folder_path, os.path.join(destination_folder, 'test', 'images'))

    move_labels(train_images, labels_folder_path, os.path.join(destination_folder, 'train', 'labels'))
    move_labels(val_images, labels_folder_path, os.path.join(destination_folder, 'val', 'labels'))
    move_labels(test_images, labels_folder_path, os.path.join(destination_folder, 'test', 'labels'))

def move_images(image_list, source_folder, destination_folder):
    for image_file in image_list:
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(destination_folder, image_file)
        shutil.move(source_path, destination_path)

def move_labels(image_list, source_folder, destination_folder):
    for image_file in image_list:
        label_file = image_file.replace('.jpg', '.txt')  # Assuming labels have the same name with .txt extension
        source_path = os.path.join(source_folder, label_file)
        destination_path = os.path.join(destination_folder, label_file)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"image {image_file} has no labels file")

def remove_images_without_labels(train_folder_path, labels_folder_path):
    # Get a list of image files in the training folder
    count = 0
    image_files = [f for f in os.listdir(train_folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    # Iterate through the image files and check if corresponding label files exist
    for image_file in image_files:
        label_file = image_file.replace('.jpg', '.txt')  # Assuming labels have the same name with .txt extension
        label_path = os.path.join(labels_folder_path, label_file)

        # If the corresponding label file does not exist, remove the image file
        if not os.path.exists(label_path):
            image_path = os.path.join(train_folder_path, image_file)
            os.remove(image_path)
            print(f"Removed {image_path} as there is no corresponding label file.")
            count+=1
    print(f"finished: removed { count} images")

        
if __name__ == "__main__":
    images_folder_path = r'C:\Users\Yaniv\Desktop\RoboWheel\carAsServer-try\new_data\r6\splitted\r6_images'
    # destination_folder = 'data/new_data/renmaed'
    labels_folder_path = r'C:\Users\Yaniv\Desktop\RoboWheel\carAsServer-try\new_data\r6\splitted\‏‏r6_labels'
    dest_folder = 'data/r6_new_data'
    # remove_images_without_labels(images_folder_path,labels_folder_path )
    # test_val_split(images_folder_path, labels_folder_path, dest_folder)
    test_val_split(images_folder_path, labels_folder_path, dest_folder, val_ratio=0.2,test_ratio=0.1)
    # rename_and_split_images(images_folder_path, dest_folder)


   
