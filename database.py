
import sensors
import time
import mqtt_client

def offlinehandler(connected, accel, magnet, gyro, alti, client):
        file = open("offline.txt", "w+")
        while not connected:
            json_data = sensors.saveSensorValuesAsJson(accel, magnet, gyro, alti)
            file.write(json_data)
            time.sleep(5)
            connected = getconnected()
        file.close()
        offline_json = open("offline.txt").readlines()
        offline_json_str = str(offline_json)
        mqtt_client.publish("/SysArch/V4/offline", offline_json_str, client)
        file.close()
        print("Offline data sent to: SysArch/V4/offline")
        connected = True
        time.sleep(0.9)
        return

def getconnected():
    #tbd.
    return False