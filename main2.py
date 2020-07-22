

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
global json_data, accel, magnet, gyro, alti, client, loggout, loggedIn
loggedIn = False
loggout = 'no'
json_data = None

def sensorvalues():
    while True:
        global json_data, accel, magnet, gyro, alti, loggout, loggedIn
        json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)  # read sensor values and save them as a JSON string
        mqtt_client.publish("/SysArch/V4", json_data, client)  # publish JSON string
        if loggout == 'q' and loggedIn:
            timestamp = time.time() *1000
            loggoutmessage = "{\"timestamp\":" + str(timestamp) + ", \"login\"= false}"         #tokenID fehlt noch
            mqtt_client.publish("/SysArch/V4/com2/web", loggoutmessage, client)
            login.answer_handler(loggedIn)

            mqtt_client.stopClient(client)
            return
def gui():
    global loggout
    while True:
        sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(0.5)


        print("***  MENU  *** \n\n")
        print("~ 1-Car Stats ~")
        print("~ 2-Air conditioning ~")
        print("~ [q]-Logout ~")

        input = raw_input("Please enter your choice: ")
        print("   ")
        print("   ")

        if input == "1":
            print("All car stats are good")
            print("   ")
            print("   ")
        elif input == "2":
            print("air conditioning is on")
            print("   ")
            print("   ")
        elif input == 'q':
            loggout = 'q'
            return


class myThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        sensorvalues()


class myThread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        gui()


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
