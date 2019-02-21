import socket


ip = ('127.0.0.1', 9516)
sk = socket.socket()
sk.bind(ip)
sk.listen(5)
print('server 开始监听')
while True:
    conn, addr =sk.accept()
    print(addr)
    while True:
        client_date = conn.recv(1024)
        if str(client_date, 'utf8') =='exit': break
        print('来自client的数据：' + str(client_date, 'utf8'))
        conn.sendall(bytes(input('server:'), encoding='utf8'))
sk.close()