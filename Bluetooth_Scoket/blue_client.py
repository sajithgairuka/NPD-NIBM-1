import socket

serverMACAddress = '00:1a:7d:da:71:10'
port = 1

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

msg = s.recv(1024)
print(msg.decode("utf-8"))