
from remote_control import*
from constants import *

def pedestrian_handler(pedestrian_size, car_speed):   
    stop()
    set_speed(INITIAL_SPEED)

def stop_sign_handler(stop_sign_size,car_speed, sleep_time = 4):
    """
    args : obj_size : area of stop sign
           sleep_time (seconds) -> time to sleep after sending stop command to car.
    Returns:
    - int: new car speed.
    """  
    stop()
    time.sleep(sleep_time)
    set_speed(INITIAL_SPEED)
    move_forward()
    return INITIAL_SPEED

def crosswalk_handler(crooswalk_sign_size,car_speed):
    set_speed(CROSSWALK_SPEED)
    move_forward()
    return CROSSWALK_SPEED

def speed_limit_handler(speed_limit):
    if speed_limit == SPEED_LIMIT_100_SIGN:
        set_speed(LIMIT_100_SPEED)
        car_speed = LIMIT_100_SPEED
        
    elif speed_limit == SPEED_LIMIT_50_SIGN:
        set_speed(LIMIT_50_SPEED)
        car_speed = LIMIT_50_SPEED
    
    move_forward()
    return car_speed
