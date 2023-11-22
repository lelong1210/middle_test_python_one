import mysql.connector

class Connectdb:
    def __init__(self) -> None:
        mydb = mysql.connector.connect(
            host="192.168.56.200",
            user="root",
            password="root",
            database="ProjecPython"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM User_In_Proxy")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

