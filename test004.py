import  socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('开始通讯了')
        while True:
            print(self.client_address)
            while True:
                client_data = self.request.recv(1024)
                print(str(client_data, 'utf8'))
                self.request.sendall(bytes(input('server:'), encoding='utf=8'))
            self.request.close()


if __name__ == '__main__':
    t1 = socketserver.ThreadingTCPServer(('127.0.0.1', 9516), MyServer)
    print('服务启动')
    t1.serve_forever()
