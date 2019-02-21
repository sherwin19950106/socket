import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9516)
sk.connect(ip_port)
while True:
    send_data =input('client:')

    sk.sendall(bytes('client1:' + send_data, encoding='utf8'))
    if send_data == 'exit':
        break
    server_reply = sk.recv(1024)
    print('来自server的消息：' + str(server_reply, 'utf8'))
sk.close()
