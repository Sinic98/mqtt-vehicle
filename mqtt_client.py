import paho.mqtt.client as mqtt
import time
# create a MQTT client
def setupClient():

    client = mqtt.Client("Pi8")
    client.username_pw_set("V4", "DE7")
    client.connect("localhost", 8884)
    print("Client connected")

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

    client.on_connect = on_connect
    client.on_publish = on_publish

    lwm = "Error: Client disconnected. Dataloss may occur!"     # last will message
    client.will_set("/SysArch/V4" + str(time.time() * 1000), lwm, 1, retain = True)
    client.reconnect_delay_set(min_delay = 1, max_delay = 15)
    client.loop_start()
    return client


def publish(topic, data, client):
    client.publish(topic, data, 2)

def subscribe(topic, client):
    client.subscribe(topic, 2)

def stopClient():
    client.loop_stop()
