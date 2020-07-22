
from time import sleep

from constants import *         # Includes addresses on I2C bus
from lsm6ds33 import LSM6DS33   # Accel & Gyro (+ temp)
from lis3mdl import LIS3MDL     # Magnetometer (+ temp)
from lps25h import LPS25H       # Barometric Pressure & Temperature
from altimu import AltIMU
import mysql.connector
import random
import threading
import sensors
import login
import mqtt_client
import database
import rfid
import sys
import os
import json
import time
from gpiozero import CPUTemperature


global json_data, accel, magnet, gyro, alti, client, loggout, connected
loggout = 'no'
json_data = None

# function which runs in thread 1
def sensorvalues():
    while True:
        global json_data, accel, magnet, gyro, alti, loggout, connected, loggedIn
        json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)  # read sensor values and save them as a JSON string
        time.sleep(1)
        mqtt_client.publish("/SysArch/V4", json_data, client)  # publish JSON string
# if not connected to the client, start the database.offlinehandler ** we dont change the variable! We didnt have time to implement that
        if connected == False:
            database.offlinehandler(connected, accel, magnet, gyro, alti, client)
#if loggout is set in the gui, loggout process starts
        if loggout == 'q':
            timestamp = time.time() *1000
            timestampstr = str(timestamp)
            loggoutmessage = "{\"timestamp\": " + timestampstr + ", \"login\": false, \"tokenID\": \"  \"}"
            mqtt_client.publish("/SysArch/V4/com2/web", loggoutmessage, client)
            print("You are logged out! Don't forget your phone :)")
            print(" ")
            print(" ")
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
# UI Methods
# car stats
        if input == "1":
            input = 't'
            while input == 't':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n*** Car stats ***\n\n")
                print("Altimeter: ")
                print("Speed: ")
                print("Temperature: ")
                print("\n******************************************\n")
                input = raw_input("Press 'b' for going back: ")
# Airconditioning
        elif input == "2":
            input = 't'
            while input == 't':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nAirconditioning\n\n")
                print("\n******************************************\n")
                input = raw_input("Press 'b' for going back: ")
# loggout UI
        elif input == 'q':
            loggout = 'q'
            return

# thread 1
class myThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        sensorvalues()

# thread 2
class myThread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        gui()


def main():
    global loggedIn, accel, magnet, gyro, alti, client, connected
    loggedIn = False
    requestsent = False

    client = mqtt_client.setupClient()
    print("Client Setup finished")
    sleep(0.1)
    connected = True

    while requestsent == False:  # runs until Request sent
        requestsent = login.rfidRequest(client, requestsent)

    while loggedIn == False:  # runs until Request is certified
        loggedIn = login.answer_handler(loggedIn)


    accel, magnet, gyro, alti = sensors.enableSensors()  # enables sensors

    lockMe = threading.Lock()

    t1 = myThread(1, "Sensordata")
    t2 = myThread2(2, "UI")

    t1.start() #start thread for reading and publishing sensor values
    t2.start() #start thread for the ui



if __name__ == "__main__":
    main()
