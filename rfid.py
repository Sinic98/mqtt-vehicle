import RFID as rfid

def RFIDRead():
    (status,uid) = rfid.MIFAREReader.MFRC522_Anticoll()
    return status, uid
