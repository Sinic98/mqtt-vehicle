import paho.mqtt.client as mqtt
from time import sleep

import random as rd


# creates a MQTT Client

client = mqtt.Client("Pi8")

client.username_pw_set("V4","DE7")
client.connect("localhost", 8884)

# print("Client connected")

def on_connect(client, userdata, flags, rc):
	print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, rc):
	print("data published \n")
	pass


client.on_connect = on_connect
client.on_publish = on_publish


client.loop_start()

while True:
    temperature = rd.random()
    sleep(1)
    print(temperature)
    client.publish("/SysArch/V4/Test", temperature)


client.loop_stop()


