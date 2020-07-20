from MFRC522 import *

def RFIDRead():
    (status,uid) = Read.MIFAREReader.MFRC522_Anticoll()
    return status, uid
