#encoding=utf-8
import socket
sock=('192.168.191.1',20072)
sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sckt.bind(sock)
sckt.listen(5)
conn,address=sckt.accept()
print('connect by',address)
while True:
    data=conn.recv(1024)
    if not data:
        break
    print(data)
    conn.send('I reserve')
sckt.close()