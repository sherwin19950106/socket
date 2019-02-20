import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9988)
sk.connect(ip_port)
sk.sendall(bytes('i am client',encoding='utf8'))
server_reply = sk.recv(1024)
print(str(server_reply,'utf8'))
sk.close()
