

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
import rfid
import sys
import termios
import tty
import gui







def main():
    loggedIn = False
    requestsent = False
    client = mqtt_client.setupClient()
    print("Client Setup finished")
    sleep(0.1)
    connected = True

    while requestsent == False:                                             #runs until Request sent
        #loggedIn = login.loginRequest(client, loggedIn)
        requestsent = login.rfidRequest(client, requestsent)
        
    while loggedIn == False:                                                #runs until Request is certified
        loggedIn = login.answer_handler(loggedIn)

    accel, magnet, gyro, alti = sensors.enableSensors()                     #enables sensors
    json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)   #read sensor values and save them as a JSON string

    mqtt_client.publish("/SysArch/V4", json_data, client)                   #publish JSON string
    if client.connected_flag == False:
        print("I am offline!")
        database.offlinehandler(client.connected_flag, accel, magnet, gyro, alti, client)
    time.sleep(0.1)

    gui()

    while loggedIn == False:
        key = inkey()
        if key == "q":
            mqtt_client.stopClient(client)
            loggedIn = login.logout(client, loggedIn)
        else:
            print("Bis Bald Welt")

        if key == "r":
            exit()


if __name__ == "__main__":
    main()





