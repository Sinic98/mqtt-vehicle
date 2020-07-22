

import json
import time
from gpiozero import CPUTemperature
import random

from time import sleep
import threading
#from _thread import start_new_thread
#import  queue

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
import os
import termios
import tty
import gui
global json_data, accel, magnet, gyro, alti, client
json_data = None

def sensorvalues():
    while True:
        global json_data, accel, magnet, gyro, alti
        json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)  # read sensor values and save them as a JSON string
        mqtt_client.publish("/SysArch/V4", json_data, client)  # publish JSON string

class myThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        global json_data#, lockMe
        #with lockMe:
            json_data = saveSensorValuesAsJson()


class myThread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        global json_data
        print("T2")

def main():
    loggedIn = False
    requestsent = False
    global client
    client = mqtt_client.setupClient()
    print("Client Setup finished")
    sleep(0.1)
    connected = True

    while requestsent == False:  # runs until Request sent
        # loggedIn = login.loginRequest(client, loggedIn)
        requestsent = login.rfidRequest(client, requestsent)

    while loggedIn == False:  # runs until Request is certified
        loggedIn = login.answer_handler(loggedIn)
    global accel, magnet, gyro, alti
    accel, magnet, gyro, alti = sensors.enableSensors()  # enables sensors

    lockMe = threading.Lock()

    t1 = myThread(1, "Sensordaten")
    t2 = myThread2(2, "Display")

    t1.start()
    t2.start()



        




if __name__ == "__main__":
    main()
