# This is my learning notes.
## What? A socket is one endpoint of a communication channel used by programs 
## The purpose? To pass data back and forth locally or across the Internet
## Sockets have two primary properties controlling the way they send data: 
### 1) the *address family* controls the OSI network layer protocol used. For example, AF_INET, AF_INET6, AF_UNIX
### 2) the *socket type* controls the transport layer protocol. For example, SOCK_DGRAM, for user datagram protocol (UDP); SOCK_STREAM, for transmission control protocol (TCP)

## Python Socket Programming Workflow
## Server End           Client End
## socket()             socket()
## bind()               |
## listen()             |
## accept()             |
## ...waiting for connection
## |                    ...establish connection by
## |                    connect()
## recv() <--request--  send()
## ...process request   |
## send()               recv()


#import the socket library
import socket
import threading
import time

#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
## AF_INET = Address Format, Internet = IP Addresses


#PORT   -reserve a port on your computer
#SERVER -return an IP address that corresponds to the supplied hostname
#ADDR   -make port and server as a tuple
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1024
#print(SERVER)
ADDR = (SERVER, PORT)
HEADER = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

#bind to the port, make the server listen 
# to requests coming from other computers on the network
s.bind(ADDR) 


##Method 1
#handle all connection between one client and one server from now to so on
def handle_client(clt, adr):
    print(f"[NEW CONNECTION] {adr} connected.")

    connected = True
    while connected:
        msg_len = clt.recv(HEADER).decode(FORMAT) #so how many bite you want to send. Introduce header
        if msg_len:
            msg_len = int(msg_len)
            msg = clt.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

        print(f"[{adr}] {msg}")
        clt.send("Message reveived".encode(FORMAT))
        
    clt.close()

#handle new connection
def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #ask server to keep listening until stop it
    while True:
        clt, adr = s.accept()
        thread = threading.Thread(target=handle_client, args=(clt,adr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")


print("[STARTING] Connection has been established")
start()


'''
##Method 2
#put the socket into listening mode
s.listen(5)
print(f"[LISTENING] Server is listening by socket on {SERVER}")

#create a loop until some error occurs
while True:
    #establish connection with client
    clt, adr = s.accept()
    print(f"[STARTING] Connection from {adr} has been established")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADER}}"+ msg

    #send message to the client
    clt.send(bytes(msg, "utf-8"))
    
    while True:
        time.sleep(5)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADER}}"+ msg
        clt.send(bytes(msg, "utf-8"))

'''