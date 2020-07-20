from MFRC522 import *

def RFIDRead():
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
