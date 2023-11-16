import multiprocessing
import subprocess


def run_driver_with_object_detection():
    """
    Execute the AI driver script which handles object detection for the car.
    """
    subprocess.run(["python", "car_AI/ai_driver.py"], shell=True)

def run_web_app():
    """
    Execute the web application script.
    """
    subprocess.run(["python", "web_app/app.py"], shell=True)

if __name__ == "__main__":
 
    car_detection_process = multiprocessing.Process(target=run_driver_with_object_detection)
    web_app_process = multiprocessing.Process(target=run_web_app)

    car_detection_process.start()
    web_app_process.start()

    car_detection_process.join()
    web_app_process.join()