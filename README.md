# Robowheel: Autonomous Toy Car with Object Detection

Robowheel is an embedded system project focused on creating an autonomous toy car with real-time object detection capabilities. Developed using C++ in the Arduino IDE for precise motor control, it integrates sensors for effective operation. Utilized an ESP32 board for image capture and Wi-Fi communication, enabling seamless data transfer. Deployed a custom YOLOv7 Tiny model for road sign, pedestrian, crosswalk, speed limit sign, and stop sign detection.

## Key Features

- **Real-time Object Detection:** Employs a custom YOLOv7 Tiny model for identifying road signs, pedestrians, crosswalks, speed limit signs, and stop signs.
- **ESP32 Integration:** Utilizes the ESP32 board for image capture and Wi-Fi communication, facilitating smooth data transfer for informed decision-making.
- **Arduino-Based Control:** Developed in C++ programming in the Arduino IDE, ensuring precise motor control and seamless sensor integration.
- **Client-side in Python:** The client-side code for interacting with the car is written in Python, enabling easy communication and control.

## Usage

This project showcases an autonomous toy car's capabilities with real-time object detection. Although replicating the hardware setup might not be feasible for everyone, you can explore and understand the project's functionalities through visual media provided.

### Visual Showcase

- **Images:** Discover images displaying the car's hardware setup and operation in the `images/` directory.
- **Video Demonstration:** 
[![Object Detection Demo Video](https://img.youtube.com/vi/nsQOkq1Gojw/0.jpg)](https://www.youtube.com/watch?v=nsQOkq1Gojw)
[![Car Driving Demo Video](https://img.youtube.com/vi/1lWNy7MTgDM/0.jpg)](https://www.youtube.com/watch?v=1lWNy7MTgDM)

Feel free to explore the codebase, review the project's architecture, and delve into specific functionalities by examining the code and documentation.

## Acknowledgements

- [OpenCV](https://opencv.org/): Used for image processing and computer vision tasks.
- [YOLOv7](https://github.com/AlexeyAB/darknet): Framework for object detection in the custom model.
- [Arduino IDE](https://www.arduino.cc/): Platform used for programming the microcontroller.
- [ESP32 Camera Web Server](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer): Library for ESP32 camera integration, enabling image capture and processing.


## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or submit pull requests to enhance this project!
