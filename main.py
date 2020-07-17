class Gyro():
    def __init__(self, id, timestamp, valueX, valueY, valueZ):
        self.id = id
        self.timestamp = timestamp
        self.valueX = valueX
        self.valueY = valueY
        self.valueZ = valueZ
class Magnetometer():
    def __init__(self, id, timestamp, valueX, valueY, valueZ):
        self.id = id
        self.timestamp = timestamp
        self.valueX = valueX
        self.valueY = valueY
        self.valueZ = valueZ
class Acceleration():
    def __init__(self, id, timestamp, valueX, valueY, valueZ):
        self.id = id
        self.timestamp = timestamp
        self.valueX = valueX
        self.valueY = valueY
        self.valueZ = valueZ
class Altimeter():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class Speed():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class Temperature():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class SteeringAngle():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class Humidity():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class Lidar():
    def __init__(self, id, timestamp, value):
        self.id = id
        self.timestamp = timestamp
        self.value = value
class LoginData():
    def __init__(self, timestamp, tokenID, login):
        self.timestamp =timestamp
        self.tokenID =tokenID
        self.login = login

import json
import time
from gpiozero import CPUTemperature
import random

import paho.mqtt.client as mqtt
from time import sleep

from constants import *         # Includes addresses on I2C bus
from lsm6ds33 import LSM6DS33   # Accel & Gyro (+ temp)
from lis3mdl import LIS3MDL     # Magnetometer (+ temp)
from lps25h import LPS25H       # Barometric Pressure & Temperature
from altimu import AltIMU
import mysql.connector
import sensors
import mqtt
import login



def main():
    loggedIn = False
    client = mqtt.setupClient()
    print("Client Setup finished")
    while loggedIn == False:
        loggedIn = login.loginRequest(client, loggedIn)

    accel, magnet, gyro, alti = sensors.enableSensors()
    print("Sensors enabled")
    #values2db()

    while loggedIn:
        json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
        #print("Values saved")
        mqtt.publish(json_data, client)
        #print("Data published")
        time.sleep(0.1)

    mqtt.stopClient()

if __name__ == "__main__":
    main()





