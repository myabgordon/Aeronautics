import matplotlib.pyplot as plt
#import board
import machine
import logging

# Setting up logging to monitor performance and errors
logging.basicConfig(level=logging.INFO)
from time import sleep

################ CONFIGS ##################################
samples_per_sec = 4  
run_time = 600  # Requested runtime in seconds
voltage_GPIO = 23
###########################################################

time_array = []   # Time array 
amps = [] # Amp array
volts = [] # Voltage array
air_speed = []  # Air speed array

sample_rate = 1 / samples_per_sec # Sample rate in samples per second
data_file = 'data.txt'  # File to save and read data

with open(data_file, 'w') as file:
    pass  # This does nothing, but it effectively clears the file

def main():
    time = 0
    while(time < (run_time*samples_per_sec)):  
        time_array.append(time)
        amps.append(get_amps(time))
        volts.append(get_voltage(time))
        air_speed.append(get_airspeed(time))
        time += sample_rate
        save_data()
        sleep(sample_rate)

def get_amps():
    return None

def get_voltage():
    try:
        logging.info("Reading voltage sensor...")
        adc = machine.ADC(voltage_GPIO)
        voltage = adc.read_u16() * 3.3 / 65535
        return round(voltage, 2)
    except Exception as e:
        logging.error(f"An error occurred while reading voltage sensor: {e}")
        return None

def get_airspeed(time):
    return None

def gps():
    return 1


def save_data():
    with open(data_file, 'a') as file:
        latest_time = time_array[-1]
        latest_amp = amps[-1]
        latest_volt = volts[-1]
        latest_speed = air_speed[-1]
        file.write(f"{latest_time}\t{latest_amp}\t{latest_volt}\t{latest_speed}\n")

if __name__ == "__main__":
    main()
    print("Script Stopped Successfully")