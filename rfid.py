import MFC522.Read as rfid

def RFIDRead():
    (status,uid) = rfid.MIFAREReader.MFRC522_Anticoll()
    return status, uid
