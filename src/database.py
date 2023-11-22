import mysql.connector

class DatabaseMysql:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="192.168.56.200",
            user="root",
            password="root",
            database="ProjecPython"
        )
        
    def insert_to_database(self, pretty_host, method,url,address,http_version,status_code):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO User_In_Proxy(pretty_host, method, url, address, http_version, status_code) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (pretty_host, method,url,address,http_version,status_code)
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def select_from_database(self):
        sql = "SELECT address, method, pretty_host, url,status_code, http_version FROM User_In_Proxy ORDER BY id DESC LIMIT 100"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult