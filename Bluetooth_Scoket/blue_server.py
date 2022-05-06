import socket

hostMACAddress = '1C:CC:D6:B4:78:48'
port = 1

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(5)

while True:
    client, address = s.accept()
    print("Connection has been established")
    client.send(bytes("Wellcome to the server!","utf-8"))