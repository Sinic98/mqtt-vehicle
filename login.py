import json
import time
import mqtt_client
class LoginData():
    def __init__(self, timestamp, tokenID):
        self.timestamp =timestamp
        self.tokenID =tokenID


def loginRequest(client, loggedIn):
    if raw_input("Do you want to log in? (yes/no)") == 'yes':
        login = LoginData(timestamp=time.time()*1000, tokenID="TOKENID EINFUEGEN")
        login_json = json.dumps(login.__dict__)
        mqtt_client.publish("/SysArch/V4/LoginRequest", login_json, client)
        print("LoginRequest")
        loggedIn = True
        time.sleep(0.9)
        return loggedIn
    else:
        time.sleep(0.5)
        loggedIn = False
        return loggedIn



