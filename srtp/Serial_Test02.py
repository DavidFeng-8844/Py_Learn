#import RPi.GPIO as GPIO
import pigpio  # 用于舵机控制
import time
import random

# Define labels and types
labels = [1, 2, 3, 4, 5]
types = ["Recyclable", "Harmful", "Organic", "Other"]

if __name__ == '__main__':

    # Create a list of random data items
    data_items = []
    for _ in range(1):  # Send 3 data items 
        data_item = [
            str(random.choice(labels)),
            "WaterBottle",
            str(11),
            str(12),
            str(13),
            str(14),
            str(random.choice(labels)),
            "WaterBottle",
            str(21),
            str(22),
            str(23),
            str(24),
            str(random.choice(labels)),
            "WaterBottle",
            str(31),
            str(32),
            str(33),
            str(34),
            ]
        data_items.append(",".join(data_item))  
        # Convert the list to a string separated by commas
        data_str = ",".join(data_items) 
        #//Write a for loop to print the data_str repeatedly
        for _ in range(1):
            print(data_str)  # Print the data string
            time.sleep(1)  # Sleep for 1 second
            # Initialize pigpio library
            pi = pigpio.pi()
            # Control the servo
            pi.set_servo_pulsewidth(17, 135)  # Replace with actual GPIO pin and position
            time.sleep(0.5)
            pi.set_servo_pulsewidth(17, 180)  # Replace with actual GPIO pin and position
            time.sleep(1.5)
            pi.set_servo_pulsewidth(17, 135)  # Replace with actual GPIO pin and position
            time.sleep(0.5)
            pi.set_servo_pulsewidth(17, 90)  # Replace with actual GPIO pin and position
            time.sleep(1.5)
            pi.set_servo_pulsewidth(17, 90)  # Replace with actual GPIO pin and position
            time.sleep(1.5)
            
