from MFRC522/Read import *

def RFIDRead():
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
