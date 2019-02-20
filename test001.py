import socket

sk =socket.socket()
ip_port = ('127.0.0.1',9988)
sk.bind(ip_port)
sk.listen(5)
conn,addr = sk.accept()
client_data = conn.recv(1024)
print(str(client_data,'utf8'))
conn.sendall(bytes('i am server',encoding='utf8'))
sk.close()