import paho.mqtt.client as mqtt
import time
import login
import json

# create a MQTT client
def setupClient():

    client = mqtt.Client("Pi8")
    client.username_pw_set("V4", "DE7")
    client.connect("localhost", 8884)
    print("Client connected")

    client.subscribe("/SysArch/V4/com2/car")
    print("Client subscribed")

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("CONNACK received with code %d." % (rc))
            client.connected_flag = True
            #client.disconnect_flag = False
        else:
            print("Connection refused with code %d." %(rc))
           # client.connected_flag = False
           # client.disconnected_flag = True

    def on_disconnect(client, userdata, rc):
        if rc!= 0:
            print("Unexpected disconnection! disconnecting reason:  " + str(rc))
            client.connected_flag = False
        else:
            print("Disconnected: " + str(rc))

        #client.connected_flag = False
       # client.disconnect_flag = True

    def on_publish(client, userdata, rc):
        print("Data published")
        pass

    def on_message(client, userdata, message):
        print "Message received: "  + message.payload
        global loginAnswer
        loginAnswer = json.loads(message.payload)
        print("ERFOLG: " + loginAnswer["certified"])
            

    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message

    lwm = "Error: Client disconnected. Dataloss may occur!"     # last will message
    client.will_set("/SysArch/V4" + str(time.time() * 1000), lwm, 1, retain = False)
    client.reconnect_delay_set(min_delay = 1, max_delay = 10)
    client.loop_start()
    return client


def publish(topic, data, client):
    client.publish(topic, data, 2)

def subscribe(topic, client):
    client.subscribe(topic, 2)

def stopClient(client):
    client.loop_stop()
