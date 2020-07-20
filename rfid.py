

def RFIDRead():
    from MFRC522.Read import *
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
