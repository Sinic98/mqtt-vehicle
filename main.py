import Klassen
import MQTT_function

client = setupClient()

loggedIn = true

while loggedIn:
    json_data = saveSensorValuesAsJson()
    publish(json_data, client)

stopClient()

