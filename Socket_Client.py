#encoding=utf-8
import socket

server=('192.168.191.1',20072)
sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sckt.connect(server)
sckt.send('hello')
data=sckt.recv(1024)
print('enco',data)