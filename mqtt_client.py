import paho.mqtt.client as mqtt
import time
import login
import json

global loginAnswer
global loginque
loginque = False

# create a MQTT client
def setupClient():
    client = mqtt.Client("Pi8")
    client.username_pw_set("V4", "DE7")
    lwm = "Error: Client disconnected. Dataloss may occur!"     # last will message
    client.will_set("/SysArch/V4/", lwm, 1, retain = False)
    client.connect("localhost", 8884)                           #connect client
    print("Client connected")

    client.subscribe("/SysArch/V4/com2/car")
    print("Client subscribed")

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("CONNACK received with code %d." % (rc))
            client.connected_flag = True
        else:
            print("Connection refused with code %d." %(rc))

    def on_disconnect(client, userdata, rc):
        if rc!= 0:
            print("Unexpected disconnection! disconnecting reason:  " )
            client.connected_flag = False
        else:
            print("Disconnected: " )

    def on_publish(client, userdata, rc):
        pass

    def on_message(client, userdata, message):

        buffer=message.payload
        global loginAnswer, loginque
        loginAnswer = json.loads(buffer)        # converts json formatted message into  object
        loginque = True


    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message
    client.on_disconnect = on_disconnect


    client.loop_start()
    return client


def publish(topic, data, client):
    client.publish(topic, data, 2)

def subscribe(topic, client):
    client.subscribe(topic, 2)

def stopClient(client):
    client.loop_stop()


