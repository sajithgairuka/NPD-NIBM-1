import socket                                       #example for server side :127.0.0.1 -l 5555 -p
import sys                                          #example for client side :127.0.0.1 5555 -p
import argparse                                     #refer "client.pdf" for before run this program
from threading import *                       

p=argparse.ArgumentParser()
p.add_argument("serverip",nargs='?',type=str) #server address
p.add_argument("-l","--ip",type=str) #Listen Ip address
p.add_argument("-p","--port",type=int)#listen port
args = p.parse_args()

def server():
    if args.ip:
        if args.port:
            print("-------------------------------------")
            print("I'm The Server !!!!!!!")
            print("Server is Listning on : " +args.ip + " : " + str(args.port))
            s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                s.bind((args.ip ,args.port))

            except socket.error as e:
                print(".................................................................................................\n")
                print(str(e))
                print("\n.................................................................................................")

            s.listen()
            conn , addr=s.accept()
            print("Connected to: " + addr[0]+ " : " + str(addr[1])+"\n............................")
            conn.send(str.encode("Welcome python Chat Server !!! \n.............................."))

            t1=Thread(target=msg , args=(conn,))
            t1.start()

            try:
                while True:
                    send=input()
                    conn.send(send.encode("utf-8"))
                    if not send:
                        conn.send("\n".encode("utf-8"))
            except:
                print("connection problem !!!! Plese Try Again !!!!!")
                sys.exit()


def client():
    if args.serverip:
        if args.port:
            print("-------------------------------------")
            print("I'm The Client !!!!!")
            print(" You are Connected to: "+ args.serverip + ":"+ str(args.port))
            c=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                c.connect((args.serverip ,args.port))

            except socket.error as e:
                print("....................................................................................................\n")
                print(str(e))
                print("\n....................................................................................................")

            t2=Thread(target=msg , args=(c,))
            t2.start()

            try:
                while True:
                    send=input()
                    c.sendall(send.encode("utf-8"))
                    if not send:
                        c.send("\n".encode("utf-8"))

            except:
                print("connection problem !!!! Plese Try Again !!!!!!!")
                sys.exit()
                                                  
def msg(conn):

    try:
        while True:
            data=conn.recv(2048)
            print(data.decode("utf-8"))
                      
    except:
        print("Connection erro !!!!! Plese Try Again !!!!!!!!")
        sys.exit()
            
server()
client()
            
