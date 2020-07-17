
import sensors

def offlinehandler(connected, accel, magnet, gyro, alti):
    if not connected:
        file = open("offline.txt", "w")
        while not connected:
            json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
            file.write(json_data)
        file.close()