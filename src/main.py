from mitmproxy import http
from mitmproxy import ctx
# from connectdb import Connectdb

import socket
import json


HOST = '192.168.56.1'  # Địa chỉ IP của server
PORT = 9999         # Cổng mà server socket lắng nghe
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
        

class ProxyServerCustom:    

    def __init__(self):
        self.ssl_bump_enabled = True

    def request(self, flow: http.HTTPFlow) -> None:
        pass

    def response(self, flow: http.HTTPFlow) -> None:

        dataProxy = DataProxy(
            str(flow.request.pretty_host),
            str(flow.request.method),
            str(flow.request.url),
            str(flow.client_conn.address[0]),
            str(flow.request.http_version),
            str(flow.response.status_code)
        )
        self.send_data(dataProxy)
        
    def send_data(self,dataProxy):
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