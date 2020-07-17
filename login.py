import json
import time
import mqtt
class LoginData():
    def __init__(self, timestamp, tokenID):
        self.timestamp =timestamp
        self.tokenID =tokenID


def loginRequest(client, loggedIn):
    if raw_input("Do you want to log in? (yes/no)") == 'yes':
        login = LoginData(timestamp=time.time()*1000, tokenID="TOKENIDEINFUEGEN")
        login_json = json.dumps(login.__dict__)
        mqtt.client.publish("/V4/LoginRequest", login_json, client)
        print("LoginRequest")
        loggedIn = True
        return loggedIn
    else:
        time.sleep(0.1)
        loggedIn = False
        return loggedIn



