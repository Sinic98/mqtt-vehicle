import paho.mqtt.client as mqtt


def setupClient():
    # creates a MQTT Client

    client = mqtt.Client("Pi8")

    client.username_pw_set("V4", "DE7")
    client.connect("localhost", 8884)

    print("Client connected")

    def on_connect(client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

    def on_publish(client, userdata, rc):
        print("data published \n")
        pass

    client.on_connect = on_connect
    client.on_publish = on_publish

    lwm = "Error: Client disconnected. Dataloss may occur!"     # last will message
    client.will_set("/SysArch/V4", lwm, QOS1)
    client.loop_start()
    return client


def publish(topic, data, client):
    client.publish(topic, data, 2)

def subscribe(topic, client):
    client.subscribe(topic, 2)

def stopClient():
    client.loop_stop()