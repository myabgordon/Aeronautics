import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin you want to read
gpio_pin = 23  # Replace with your GPIO pin number

# Set up the GPIO pin as an input
GPIO.setup(gpio_pin, GPIO.IN)

try:
    while True:
        # Read the digital value on the GPIO pin
        input_value = GPIO.input(gpio_pin)
        print(f"Digital Value: {input_value}")

        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()