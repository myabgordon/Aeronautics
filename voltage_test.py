import board
import machine
import logging

logging.basicConfig(level=logging.INFO)
from time import sleep


voltage_GPIO = 23

print("Starting Voltage Sensor Test")

while True:
    sleep(1)
    try:
        adc = machine.ADC(voltage_GPIO)
        voltage = adc.read_u16() * 3.3 / 65535
        print(voltage)
    except Exception as e:
        logging.error(f"An error occurred while reading voltage sensor: {e}")