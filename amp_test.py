import board
import machine
import logging

logging.basicConfig(level=logging.INFO)
from time import sleep


amps_GPIO = 22

print("Starting Current Sensor Test")

while True:
    sleep(1)
    try:
        adc = machine.ADC(amps_GPIO)
        amps = adc.read_u16() * 3.3 / 65535
        print(amps)
    except Exception as e:
        logging.error(f"An error occurred while reading current sensor: {e}")