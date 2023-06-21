# This is tcpclient.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get server's IP address
server = "192.168.4.26"

# set destination port
port = 10000

# connection to hostname on the port.
s.connect((server, port))

# send message. The string needs to be converted to bytes.
message = input("Please type your message to the server here ->")
s.send(message.encode())

# Receive no more than 1024 bytes
msg = s.recv(1024)

print("received: " + msg.decode())

# Close connection
s.close()

