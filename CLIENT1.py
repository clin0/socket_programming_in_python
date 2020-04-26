# This is my learning notes.
## What? A socket is one endpoint of a communication channel used by programs 
## The purpose? To pass data back and forth locally or across the Internet
## Sockets have two primary properties controlling the way they send data: 
### 1) the *address family* controls the OSI network layer protocol used. For example, AF_INET, AF_INET6, AF_UNIX
### 2) the *socket type* controls the transport layer protocol. For example, SOCK_DGRAM, for user datagram protocol (UDP); SOCK_STREAM, for transmission control protocol (TCP)


#import the socket library
import socket


#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## AF_INET = Address Format, Internet = IP Addresses


#PORT   -reserve a port on your computer
#CLIENT -return an IP address that corresponds to the supplied hostname
#ADDR   -make port and server as a tuple
CLIENT = socket.gethostbyname(socket.gethostname()) # 192.168.56.1 is my IP address currently
PORT = 1024
ADDR = (CLIENT, PORT)
HEADER = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

s.connect(ADDR)

##Method 1
def send(msg):
    completed_info = msg.encode(FORMAT)
    msg_len = len(completed_info)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    s.send(send_length)
    s.send(completed_info)
    print(s.recv(2048).decode(FORMAT))

send("Hello, this is just for testing")

send("Hello World!")
send("This is SIYI!")
input()
send("Well, bye now!")
send(DISCONNECT_MESSAGE)




'''
##Method 2
completed_info = ''
new_info = True
while True:
    msg = s.recv(16) # just bits number. You can change to any number of bits
    if new_info:
        print(f"New message length: {msg[:HEADER]}")
        msg_len = int(msg[:HEADER])
        new_info = False

    completed_info += msg.decode("utf-8") 

    if len(completed_info)-HEADER == msg_len:
        print("Information is revieved completely.")
        print(completed_info[HEADER:])
        new_info = True
        completed_info = '' 

print(completed_info)

'''