import numpy as np
import serial
import time
import matplotlib.pyplot as plt

def getData():
    ser = serial.Serial('/dev/ttyACM7', 9600)
    sensorReadings = []
    start = time.time()
    current = time.time()
    while current - start < 10:
        data =ser.readline()
        sensorReadings.append(float(data))
        current = time.time()
    return sensorReadings

def plotter(sensorReadings):
    plt.plot(sensorReadings)
    plt.ylabel('EEG Sensor sensorReadings')
    plt.show()

if __name__ == '__main__':
    sensorReadings = getData()
    plotter(sensorReadings)
