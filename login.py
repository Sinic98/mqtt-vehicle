import json
import time
import mqtt_client
import rfid

class LoginData():
    def __init__(self, timestamp, tokenID, login):
        self.timestamp =timestamp
        self.tokenID =tokenID
        self.login = login

class LoginConfirm():
    def __init__(self, certified):
        #self.timestamp = timestamp
        #self.login = login
        self.certified = certified
        #self.tokenID = tokenID
        #self.user = user

rightLogin = LoginConfirm(True)       

def loginRequest(client, requestsent):
    if raw_input("Do you want to log in? (yes/no)") == 'yes':
        login = LoginData(timestamp=time.time()*1000, tokenID="TOKENID EINFUEGEN", login = True)
        login_json = json.dumps(login.__dict__)
        mqtt_client.publish("V4/com2/web", login_json, client)
        print("LoginRequest")
        requestsent = True
        time.sleep(0.9)
        return requestsent
    else:
        time.sleep(0.5)
        requestsent = False
        return requestsent

def rfidRequest(client):
    
    uid = ""
    while uid == "":
        (status, uid) = rfid.RFIDRead()
    
   
    login = LoginData(timestamp=time.time()*1000, tokenID = uid, login = True)
    login_json = json.dumps(login.__dict__)
    print(login_json)
        
    mqtt_client.publish("/SysArch/V4/com2/web", login_json, client)
    print("Login Request sent")

def answer_handler(loggedIn):
    x = True
    while mqtt_client.loginAnswer == None:
        if x:
            print("Warte....")
            x = False
    #global mqtt_client.loginAnswer
    print("Schleife raus")
    print(mqtt_client.loginAnswer["certified"])
    #loggedIn = true
    return loggedIn
            
            

def logout(client, loggedIn):
    login = LoginData(timestamp=time.time()*1000, tokenID=" ", login = False)
    login_json = json.dumps(login.__dict__)
    mqtt_client.publish("V4/com2/web", login_json, client)
    print("log out succesfull")
    loggedIn = False
    return loggedIn



