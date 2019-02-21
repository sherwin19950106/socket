import socket


ip = ('127.0.0.1', 9516)
sk = socket.socket()
sk.bind(ip)
sk.listen(5)
print('server 开始监听')
conn, addr =sk.accept()
client_date = conn.recv(1024)
print('address:' + str(addr))
print('来自client的数据：' + str(client_date, 'utf8'))
conn.sendall(bytes('i am server',encoding='utf8'))
sk.close()