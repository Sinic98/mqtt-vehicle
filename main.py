

import json
import time
from gpiozero import CPUTemperature
import random

from time import sleep

from constants import *         # Includes addresses on I2C bus
from lsm6ds33 import LSM6DS33   # Accel & Gyro (+ temp)
from lis3mdl import LIS3MDL     # Magnetometer (+ temp)
from lps25h import LPS25H       # Barometric Pressure & Temperature
from altimu import AltIMU
import mysql.connector
import sensors
import login
import mqtt_client
import database


def main():
    loggedIn = False
    client = mqtt_client.setupClient()
    print("Client Setup finished")
    sleep(0.1)
    connected = True
    while loggedIn == False:
        loggedIn = login.loginRequest(client, loggedIn)
    print("Login succesfull!")
    accel, magnet, gyro, alti = sensors.enableSensors()
    print("Sensors enabled")
    #values2db()

    while loggedIn:
        json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)

        mqtt_client.publish("/SysArch/V4", json_data, client)
        connected = False
        if connected == False:
            database.offlinehandler(connected, accel, magnet, gyro, alti, client)
        time.sleep(0.1)

    mqtt_client.stopClient()

if __name__ == "__main__":
    main()





