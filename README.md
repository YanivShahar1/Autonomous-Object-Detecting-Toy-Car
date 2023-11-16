# Robowheel: Autonomous Toy Car with Object Detection

Robowheel is an embedded system project focused on creating an autonomous toy car with real-time object detection capabilities. Developed in C using the Arduino IDE, it integrates sensors for precise motor control. Utilized an ESP32 board for image capture and Wi-Fi communication, enabling seamless data transfer. Deployed a custom YOLOv7 Tiny model for road sign, pedestrian, crosswalk, speed limit sign, and stop sign detection.

## Key Features

- **Real-time Object Detection:** Employs a custom YOLOv7 Tiny model for identifying road signs, pedestrians, crosswalks, speed limit signs (50 and 100), and stop signs.
- **ESP32 Integration:** Utilizes the ESP32 board for image capture and Wi-Fi communication, facilitating smooth data transfer for informed decision-making.
- **Arduino-Based Control:** Developed in C programming on the Arduino IDE, ensuring precise motor control and seamless sensor integration.

## Usage

This project showcases an autonomous toy car's capabilities with real-time object detection. Although replicating the hardware setup might not be feasible for everyone, you can explore and understand the project's functionalities through visual media provided.

### Visual Showcase

- **Images:** Discover images displaying the car's hardware setup and operation in the `images/` directory.
- **Video Demonstration:** Watch a video demonstration of the car's operation [here](link-to-video).

Feel free to explore the codebase, review the project's architecture, and delve into specific functionalities by examining the code and documentation.

## Acknowledgements

- [OpenCV](https://opencv.org/): Used for image processing and computer vision tasks.
- [YOLOv7](https://github.com/AlexeyAB/darknet): Framework for object detection in the custom model.
- [Arduino IDE](https://www.arduino.cc/): Platform used for programming the microcontroller.
- [ESP32 Camera Web Server](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer): Library for ESP32 camera integration, enabling image capture and processing.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or submit pull requests to enhance this project!
