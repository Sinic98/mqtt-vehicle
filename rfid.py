from MFRC522-python import *

def RFIDRead():
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
