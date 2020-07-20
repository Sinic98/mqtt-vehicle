

def RFIDRead():
    from MFRC522.Read 
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    return status, uid
