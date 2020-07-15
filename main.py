import Klassen
import MQTT_function

client = setupCLient()

loggedIn = true

while loggedIn:
    json_data = saveSensorValuesAsJson()
    publish(json_data, client)

stopClient()

