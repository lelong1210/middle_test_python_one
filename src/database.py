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
        sql = "SELECT address, method, pretty_host, url,status_code, http_version FROM User_In_Proxy ORDER BY id DESC"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    def delete_all(self):
        sql = "DELETE FROM User_In_Proxy"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        self.mydb.commit()
        return True
    def delete_where(self, query):
        sql = "DELETE FROM User_In_Proxy WHERE address LIKE %s OR pretty_host LIKE %s"
        mycursor = self.mydb.cursor()
        pattern = '%' + query + '%'
        mycursor.execute(sql, (pattern, pattern,))
        self.mydb.commit()
        # return True
    def search(self,query):
        sql = "SELECT address, method, pretty_host, url,status_code, http_version FROM User_In_Proxy  WHERE address LIKE %s OR pretty_host LIKE %s ORDER BY id DESC"
        mycursor = self.mydb.cursor()
        pattern = '%'+query+'%'
        mycursor.execute(sql, (pattern,pattern,))
        myresult = mycursor.fetchall()
        return myresult
    # def search_where_client_or_host