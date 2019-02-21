import socket

sk = socket.socket()
ip = ('127.0.0.1', 9516)
sk.connect(ip)
while True:
    sk.sendall(bytes('我是3号', encoding='utf8'))
    server_data = sk.recv(1024)
    print('server:' + str(server_data,'utf8'))
sk.close()
