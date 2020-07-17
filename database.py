
import sensors

def offlinehandler(connected):
    if not connected:
        file = open("offline.txt", "r")
        while not connected:
            json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
            file.write(json_data)
        file.close()