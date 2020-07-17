
import sensors
import time
import mqtt_client

def offlinehandler(connected, accel, magnet, gyro, alti, client):
    if not connected:
        file = open("offline.txt", "w+")
        while not connected:
            json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
            file.write(json_data)
            time.sleep(1)
            json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
            file.write(json_data)
            time.sleep(1)
            connected = True
        file.close()
        offline_json = open("offline.txt").readlines()
        offline_json_str = str(offline_json)
        mqtt_client.publish("/SysArch/V4/offline", offline_json_str, client)
        file.close()
