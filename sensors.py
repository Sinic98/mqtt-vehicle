
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


global x
x=0.1
# enable sensors
def enableSensors():
    # accel
    accel = AltIMU()
    accel.enable_accelerometer()

    # magnet
    magnet = AltIMU()
    magnet.enable_magnetometer()

    # gyro
    gyro = AltIMU()
    gyro.enable_gyroscope()

    # altitude
    alti = AltIMU()
    alti.enable_barometer()

    return accel, magnet, gyro, alti


def saveSensorValuesAsJson(accel, magnet, gyro, alti):
    class Gyro():
        def __init__(self, name, timestamp, valueX, valueY, valueZ):
            self.name = name
            self.timestamp = timestamp
            self.valueX = valueX
            self.valueY = valueY
            self.valueZ = valueZ

    class Magnetometer():
        def __init__(self, name, timestamp, valueX, valueY, valueZ):
            self.name = name
            self.timestamp = timestamp
            self.valueX = valueX
            self.valueY = valueY
            self.valueZ = valueZ

    class Acceleration():
        def __init__(self, name, timestamp, valueX, valueY, valueZ):
            self.name = name
            self.timestamp = timestamp
            self.valueX = valueX
            self.valueY = valueY
            self.valueZ = valueZ

    class Altimeter():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class Speed():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class Temperature():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class SteeringAngle():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class Humidity():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class Lidar():
        def __init__(self, name, timestamp, value):
            self.name = name
            self.timestamp = timestamp
            self.value = value

    class LoginData():
        def __init__(self, timestamp, tokenID, login):
            self.timestamp = timestamp
            self.tokenID = tokenID
            self.login = login


    # save sensor values in variables

    # simulate lidar value
    #lidarvalue = random.randint(200, 220)
    global x
    a = math.sin(x)
    x = x + 0.1
    lidarvalue = a
    # simulate humidity

   # humidityvalue = random.randint(20, 60)
    x = x + 0.1
    b = math.sin(x)
    humidityvalue = b

    # simulate steering angle value
    firstrun = 1
    if firstrun == 1:
        oldsteeringAnglevalue = 0
        steeringAnglevalue = 0
        firstrun = 0
    else:
        steeringAnglevalue = random.uniform(oldsteeringAnglevalue + 0.3, oldsteeringAnglevalue - 0.3)
        oldsteeringAngle = steeringAnglevalue

    cputemperaturevalue = CPUTemperature()

    # simulate speed value
    firstrun2 = 1
    if firstrun2 == 1:
        speed0 = 0
        firstrun2 = 0
        speed1 = speed0 + 3
        speedvalue = random.randint(speed0, speed1)
    else:
        speed0 = 3
        speed1 = speed0 + 2
        speedvalue = random.randint(speed0, speed1)

    altimetervalue = alti.getAltitude()

    gyrovalue = gyro.getGryoscopeMDPS()
    gyrovaluex = gyrovalue[0]
    gyrovaluey = gyrovalue[1]
    gyrovaluez = gyrovalue[2]

    magnetvalue = magnet.getMagnetometerRaw()
    magentvaluex = magnetvalue[0]
    magnetvaluey = magnetvalue[1]
    magnetvaluez = magnetvalue[2]

    accelerationvalue = accel.getAccelerometerRaw()
    accelerationvaluex = accelerationvalue[0]
    accelerationvaluey = accelerationvalue[1]
    accelerationvaluez = accelerationvalue[2]

    # safe data in object
    # timestamp in ms since epoch

    # one value data
    lidar = Lidar(name="Lidar", timestamp=time.time() * 1000, value=lidarvalue)  # simulated value
    humidity = Humidity(name="Humidity", timestamp=time.time() * 1000, value=humidityvalue)  # simulated value
    steeringAngle = SteeringAngle(name="SteeringAngle", timestamp=time.time() * 1000,
                                  value=steeringAnglevalue)  # simulated value
    cputemperature = Temperature(name="Temperature", timestamp=time.time() * 1000,
                                 value=cputemperaturevalue.temperature)  # real value
    speed = Speed(name="Speed", timestamp=time.time() * 1000, value=speedvalue)  # simulated value
    altimeter = Altimeter(name="Altimeter", timestamp=time.time() * 1000, value=altimetervalue)  # real value

    # several value data
    gyro = Gyro(name="Gyro", timestamp=time.time() * 1000, valueX=gyrovaluex, valueY=gyrovaluey,
                valueZ=gyrovaluez)  # real value
    magnetometer = Magnetometer(name="Magnetometer", timestamp=time.time() * 1000, valueX=magentvaluex,
                                valueY=magnetvaluey, valueZ=magnetvaluez)  # real value
    acceleration = Acceleration(name="Acceleration", timestamp=time.time() * 1000, valueX=accelerationvaluex,
                                valueY=accelerationvaluey, valueZ=accelerationvaluez)  # real value

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

    json_data = "{\"SensorValue1\": [" + lidar_data + "," + humidity_data + "," + steeringAngle_data + "," + temperature_data + "," + speed_data + "," + altimeter_data + "]" + "," "\"SensorValue3\": [" + gyro_data + "," + magnetometer_data + "," + acceleration_data + "]}"
    return json_data