import json
import time
class LoginData():
    def __init__(self, timestamp, username, password, tokenID):
        self.timestamp =timestamp
        self.username =username
        self.tokenID =tokenID


def loginRequest(client,loggedIn):
    
    loginRequest = "no" 
    loginRequest = input("Do you want to use the vehicle? (yes/no)")    # wird ersetzt durch RFID
    if loginRequest == "yes":
        client.publish("/V4/loginRequest", loginRequest)
        print("Login request sent to webserver")
        loginAnswer = "validated"           # wird durch antwort von Webgruppe ersetzt"
        if loginAnswer == "validated":
            loggedIn = True
            print("log in succesfull")
            return loggedIn
        else:
            print("log in failed, you are not entiteled to use this vehicle!")
            loggedIn = False
            return loggedIn







