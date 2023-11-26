from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from database import DatabaseMysql
import socket
import json
import threading
from database import DatabaseMysql

# Địa chỉ và cổng của server
HOST = '0.0.0.0'
PORT = 1234

class DataProxy:
    def __init__(self, pretty_host, method, url, address, http_version, status_code):
        self.pretty_host = pretty_host
        self.method = method
        self.url = url
        self.address = address
        self.http_version = http_version
        self.status_code = status_code

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1395, 737)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 690, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(500, 690, 181, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 1351, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(960, 10, 291, 31))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(880, 690, 181, 31))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(840, 10, 111, 20))
        self.label.setObjectName("label")
        self.pushButton_delete_where = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete_where.setGeometry(QtCore.QRect(690, 690, 181, 31))
        self.pushButton_delete_where.setObjectName("pushButton_delete_where")
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 700)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "UPDATE TABLE"))
        self.pushButton_delete.setText(_translate("Dialog", "DELETE ALL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "pretty_host"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "method"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "url"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "address"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "http_version"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "status_code"))
        self.pushButton_search.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Client Or Server"))
        self.pushButton_delete_where.setText(_translate("Dialog", "DELETE Client Or Server"))

        self.pushButton.clicked.connect(self.load_data)
        self.pushButton_delete.clicked.connect(self.delete_all_data)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_delete_where.clicked.connect(self.delete_where)
        # self.tableWidget.cellClicked.connect(self.cell_clicked)
    def delete_where(self):
        databaseMysql = DatabaseMysql()
        databaseMysql.delete_where(query=self.plainTextEdit.toPlainText())
        self.load_data()
    def search(self):
        # xóa bảng
        self.tableWidget.setRowCount(0)
        databaseMysql = DatabaseMysql()
        data = databaseMysql.search(query=self.plainTextEdit.toPlainText())

        for row_number,row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def load_data(self):
        # xóa bảng
        self.tableWidget.setRowCount(0)
        
        databaseMysql = DatabaseMysql()
        data = databaseMysql.select_from_database()

        for row_number,row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)

            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        # self.tableWidget.resiz
        print("SUCCESS")
    def delete_all_data(self):
        databaseMysql = DatabaseMysql()
        databaseMysql.delete_all()
        self.tableWidget.setRowCount(0)

def process_class(my_class,Ui_Dialog):
    # Xử lý đối tượng class ở đây, ví dụ: hiển thị thông tin
    print("Received class instance:")
    print(f"[pretty_host] {my_class.pretty_host}")
    print(f"[method] {my_class.method}")
    print(f"[url] {my_class.url}")
    print(f"[address] {my_class.address}")
    print(f"[http_version] {my_class.http_version}")
    print(f"[status_code] {my_class.status_code}")

    databaseMysql = DatabaseMysql()
    databaseMysql.insert_to_database(
        my_class.pretty_host, 
        my_class.method, 
        my_class.url, 
        my_class.address,
        my_class.http_version, 
        my_class.status_code
    )
    Ui_Dialog.load_data()


def handle_client(client_socket,Ui_Dialog):
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode('utf-8')

    if data:
        try:
            # Giải mã dữ liệu JSON
            json_data = json.loads(data)

            # Tạo đối tượng class từ dữ liệu JSON
            my_class = DataProxy(
                json_data['pretty_host'],
                json_data['method'],
                json_data['url'],
                json_data['address'],
                json_data['http_version'],
                json_data['status_code']
            )

            # Xử lý đối tượng class
            process_class(my_class,Ui_Dialog)

        except json.JSONDecodeError as e:
            print("Invalid JSON data:", data)
        except Exception as e:
            print("Error occurred while processing client data:", str(e))

    # Đóng kết nối
    client_socket.close()


def start_server(Ui_Dialog):
    # Tạo socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Server is listening on {}:{}".format(HOST, PORT))

    while True:
        # Chấp nhận kết nối từ client
        client_socket, addr = server_socket.accept()
        print("Client connected from:", addr)

        # Tạo một luồng riêng biệt để xử lý kết nối từ client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,Ui_Dialog,))
        client_thread.start()

# Khởi động server


if __name__ == "__main__":


    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    socket_threading = threading.Thread(target=start_server,args=(ui,))
    socket_threading.start()

    Dialog.show()
    sys.exit(app.exec_())

