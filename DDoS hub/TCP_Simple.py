import socket
class SimpleTcp(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def Connect(self, ip, port):
        self.sock.connect((ip, port))
    def SendByte(self, data):
        if type(data) != bytes:
            data = str(data).encode()
        self.sock.sendall(data)


class MultiSocketTcp(object):
    def __init__(self):
        self.sock_list = []
        for x in range(150):
            self.sock_list.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    def Connect(self, ip, port):
        for sock in self.sock_list:
            sock.connect((ip, port))
    def SendByte(self, data):
        if type(data) != bytes:
            data = str(data).encode()
        for sock in self.sock_list:
            sock.sendall(data)




