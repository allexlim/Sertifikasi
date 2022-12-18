import mysql.connector

class connectionData:
    def newConnection():
        connectThis = mysql.connector.connect(
            user = "root",
            password =  "",
            host =  "localhost",
            database = "perpustakaan"
        )
        return connectThis

def hurufBesar(kapital):  
    kapital = kapital.upper()
    return kapital