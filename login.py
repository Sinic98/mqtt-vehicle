import json
import time
import mqtt_client
class LoginData():
    def __init__(self, timestamp, tokenID, login):
        self.timestamp =timestamp
        self.tokenID =tokenID
        self.login = login


def loginRequest(client, loggedIn):
    if raw_input("Do you want to log in? (yes/no)") == 'yes':
        login = LoginData(timestamp=time.time()*1000, tokenID="TOKENID EINFUEGEN", login = True)
        login_json = json.dumps(login.__dict__)
        mqtt_client.publish("V4/com2/web", login_json, client)
        print("LoginRequest")
        loggedIn = True
        time.sleep(0.9)
        return loggedIn
    else:
        time.sleep(0.5)
        loggedIn = False
        return loggedIn

def logout(client, loggedIn):
    login = LoginData(timestamp=time.time()*1000, tokenID=" ", login = False)
    login_json = json.dumps(login.__dict__)
    mqtt_client.publish("V4/com2/web", login_json, client)
    print("log out succesfull")
    loggedIn = False
    return loggedIn



