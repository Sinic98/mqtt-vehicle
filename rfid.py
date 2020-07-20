from MFRC522/Read import *

def RFIDRead():
    (status,uid) = rfid.MIFAREReader.MFRC522_Anticoll()
    return status, uid
