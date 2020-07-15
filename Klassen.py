#Klassen
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

from time import sleep

from lsm6ds33 import LSM6DS33
from lis3mdl import LIS3MDL
from lps25h import LPS25H

    #enable sensors
def enableSensors():
     imu = LSM6DS33()
     imu.enableLSM()

     magnet = LIS3MDL()
     magnet.enableLIS()
     baro = LPS25H()
     baro.enableLPS()

def saveSensorValuesAsJson():
    #save sensor values in variables

    #simulate lidar value
    lidarvalue = random.randint(200,220)

    #simulate humidity
    humidityvalue= random.randint(20, 60)

    #simulate steering angle value
    firstrun =1
    if firstrun == 1:
        oldsteeringAnglevalue = 0
        steeringAnglevalue= 0
        firstrun = 0
    else:
        steeringAnglevalue= random.uniform(oldsteeringAnglevalue + 0.3, oldsteeringAnglevalue -0.3)
        oldsteeringAngle = steeringAnglevalue

    cputemperaturevalue = CPUTemperature()

    #simulate speed value
    firstrun2 =1
    if firstrun2 == 1:
        speed0=0
        firstrun2=0
        speed1= speed0 + 3
        speedvalue= random.randint(speed0, speed1)
    else:
        speed0 = 3
        speed1= speed0+2
        speedvalue =random.randint(speed0,speed1)

    altimetervalue= baro.getAltitude()

    gyrovalue = imu.getGyroscopeRaw()
    gyrovaluex= gyrovalue[0]
    gyrovaluey= gyrovalue[1]
    gyrovaluez= gyrovalue[2]

    magnetvalue= magnet.getMagnetometerRaw()
    magentvaluex= magnetvalue[0]
    magnetvaluey= magnetvalue[1]
    magnetvaluez= magnetvalue[2]

    accelerationvalue =imu.getAccelerometerRaw()
    accelerationvaluex= accelerationvalue[0]
    accelerationvaluey= accelerationvalue[1]
    accelerationvaluez= accelerationvalue[2]



    # safe data in object
    # timestamp in ms since epoch

    #one value data
    lidar = Lidar(id="Lidar", timestamp=time.time()*1000, value=lidarvalue)     #simulated value
    humidity = Humidity(id="Humidity", timestamp=time.time()*1000, value=humidityvalue)     #simulated value
    steeringAngle = SteeringAngle(id="SteeringAngle", timestamp=time.time()*1000, value=steeringAnglevalue)     #simulated value
    cputemperature = Temperature(id="CPU-Temperature", timestamp=time.time()*1000, value=cputemperaturevalue.temperature)         #real value
    speed = Speed(id="Speed", timestamp=time.time()*1000, value=speedvalue) #simulated value
    altimeter = Altimeter(id="Altimeter", timestamp=time.time()*1000, value=altimetervalue)             #real value

    #several value data
    gyro = Gyro(id="Gyro", timestamp=time.time()*1000, valueX=gyrovaluex, valueY=gyrovaluey,  valueZ=gyrovaluez) #real value
    magnetometer = Magnetometer(id="Magnetometer", timestamp=time.time()*1000, valueX=magentvaluex, valueY=magnetvaluey,  valueZ=magnetvaluez) #real value
    acceleration = Acceleration(id="Acceleration", timestamp=time.time()*1000, valueX=accelerationvaluex, valueY=accelerationvaluey,  valueZ=accelerationvaluez) #real value


    # safe data in json formatted string
    lidar_data = json.dumps(lidar.__dict__)
    humidity_data = json.dumps(humidity.__dict__)
    steeringAngle_data = json.dumps(steeringAngle.__dict__)
    temperature_data = json.dumps(cputemperature.__dict__)
    speed_data = json.dumps(speed.__dict__)
    altimeter_data = json.dumps(altimeter.__dict__)
    gyro_data = json.dumps(gyro.__dict__)
    magnetometer_data = json.dumps(magnetometer.__dict__)
    acceleration_data = json.dumps(acceleration.__dict__)

    json_data = lidar_data + "," + humidity_data + "," + steeringAngle_data + "," + temperature_data + "," + speed_data + "," + altimeter_data + "," + gyro_data + "," + magnetometer_data + "," + acceleration_data
    return json_data


