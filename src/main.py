from mitmproxy import http
from mitmproxy import ctx
# from connectdb import Connectdb

import socket
import json


HOST = '192.168.56.1'  # Địa chỉ IP của server
PORT = 9999         # Cổng mà server socket lắng nghe
array_all_connect=[]
array_Data_Proxy=[]


class DataProxy:
    def __init__(self, pretty_host, method,url,address,http_version,status_code):
        self.pretty_host = pretty_host
        self.method = method
        self.url = url
        self.address = address
        self.http_version = http_version
        self.status_code = status_code
    def dispplay(self):
        print(f"[pretty_host] {self.pretty_host}")
        print(f"[method] {self.method}")
        print(f"[url] {self.url}")
        print(f"[address] {self.address}")
        print(f"[http_version] {self.http_version}")
        print(f"[status_code] {self.status_code}")

        file_path = "./log.txt"
        with open(file_path, "a") as file:
            file.write(self.pretty_host+" ")
            file.write(self.method+" ")
            file.write(self.url+" ")
            file.write(self.address+" ")
            file.write(self.http_version+" ")
            file.write(self.status_code+"\n")
        

class ProxyServerCustom:    

    def __init__(self):
        self.ssl_bump_enabled = True

    def request(self, flow: http.HTTPFlow) -> None:
        # Xử lý yêu cầu trước khi gửi đến máy chủ
        # print(f"[HOST] {flow.request.pretty_host}")
        # print(f"[METHOD]: {flow.request.method}")
        # print(f"[URL]{flow.request.url}")
        # print(f"[ADDRESS]{flow.client_conn.address}")
        
        array_Data_Proxy.append(str(flow.request.pretty_host))
        array_Data_Proxy.append(str(flow.request.method))
        array_Data_Proxy.append(str(flow.request.url))
        array_Data_Proxy.append(str(flow.client_conn.address))


    def response(self, flow: http.HTTPFlow) -> None:
        # Xử lý phản hồi từ máy chủ trước khi gửi đến ứng dụng
        # print(f"[SERVER TO CLIENT] {flow.response.headers}")

        # ProxyServerCustom.array_host.append(flow.request.content.decode("utf-8"))
        # print(f"[COOKIE] {flow.response.cookies}")
        # print(f"[TEXT] {flow.response.text}")
        array_Data_Proxy.append(str(flow.request.http_version))
        array_Data_Proxy.append(str(flow.response.status_code))

        dataProxy = DataProxy(
            array_Data_Proxy[0],
            array_Data_Proxy[1],
            array_Data_Proxy[2],
            array_Data_Proxy[3],
            array_Data_Proxy[4],
            array_Data_Proxy[5]
        )
        
        dataProxy.dispplay()    
        array_Data_Proxy.clear()

        try:
            HOST = '192.168.56.1'
            PORT = 1234
            # Tạo socket client
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            # Mã hóa dữ liệu JSON thành chuỗi
            json_data = json.dumps(
                {
                    'pretty_host':dataProxy.pretty_host, 
                    'method':dataProxy.method,
                    'url':dataProxy.url,
                    'address':dataProxy.address,
                    'http_version':dataProxy.http_version,
                    'status_code':dataProxy.status_code
                }
            )

            # Gửi dữ liệu cho server
            client_socket.sendall(json_data.encode('utf-8'))
            # Đóng kết nối
            client_socket.close()
        except Exception as e:
            print("ERROR",e)

        # array_Data_Proxy.clear()
        # connectdb = Connectdb()        




addons = [
    ProxyServerCustom()
]

def start_proxy():
    ctx.log.info("Bắt đầu proxy server...")
    from mitmproxy.tools.main import mitmdump
    import pickle
    mitmdump(['-s', __file__] + ctx.argv[1:])

if __name__ == '__main__':
    start_proxy()