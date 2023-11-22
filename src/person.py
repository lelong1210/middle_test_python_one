import socket
import json

# Địa chỉ và cổng của server
HOST = 'localhost'
PORT = 1234

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def send_class(my_class):
    # Tạo socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Chuyển đổi đối tượng class thành dữ liệu JSON
    json_data = json.dumps({'name': my_class.name, 'age': my_class.age})

    # Gửi dữ liệu JSON cho server
    client_socket.sendall(json_data.encode('utf-8'))

    # Đóng kết nối
    client_socket.close()

# Tạo một đối tượng class
my_class = MyClass("John Doe", 30)

# Gửi đối tượng class cho server
send_class(my_class)