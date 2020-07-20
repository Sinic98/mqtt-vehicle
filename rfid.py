from MFRC522 import Read

def RFIDRead():
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
