import Klassen
import MQTT_function

setupCLient()

loggedIn = true

while loggedIn
    publish(saveSensorValuesAsJson())

stopClient()

