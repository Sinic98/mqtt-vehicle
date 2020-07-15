import paho.mqtt.client as mqtt
from time import sleep

import random as rd

def setupClient():
    # creates a MQTT Client

    client = mqtt.Client("Pi8")

    client.username_pw_set("V4","DE7")
    client.connect("localhost", 8884)

    print("Client connected")

    def on_connect(client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

    def on_publish(client, userdata, rc):
        print("data published \n")
        pass

    client.on_connect = on_connect
    client.on_publish = on_publish
    
    
    #lwm = "Error: Client disconnected!"     # last will message
    #client.will_set("/SysArch/V4/Test", lwm, QOS1)

    client.loop_start()
    return client

def publish(json_data, client):
    print(json_data)
    client.publish("/SysArch/V4/Test", json_data)

def stopClient():
    client.loop_stop()


setupClient()
publish("hi")
