
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
            file.close()
            offline_json = open("offline.txt").readlines()
            print(offline_json)
            print("Hier sollte es stehen")
            mqtt_client.publish("/SysArch/V4/offline", offline_json, client)
        file.close()
