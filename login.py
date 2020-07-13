import json
import time
class LoginData():
    def __init__(self, timestamp, username, password, tokenID):
        self.timestamp =timestamp
        self.username =username
        self.tokenID =tokenID


username1= input("User: ")
password1= input("Password: ")
id= "sssss"

logindata=LoginData(timestamp= time.time()*1000, username=username1, password = password1, tokenID = id)
logindatajson=json.dumps(logindata.__dict__)
print(logindatajson)