import Klassen
import MQTT_function

setupCLient()

loggedIn = true

while loggedIn
    json_data = saveSensorValuesAsJson()
    publish(json_data)

stopClient()

