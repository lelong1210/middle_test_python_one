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

def process_class(my_class):
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


def handle_client(client_socket):
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
            process_class(my_class)

        except json.JSONDecodeError as e:
            print("Invalid JSON data:", data)
        except Exception as e:
            print("Error occurred while processing client data:", str(e))

    # Đóng kết nối
    client_socket.close()


def start_server():
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
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Khởi động server
start_server()
