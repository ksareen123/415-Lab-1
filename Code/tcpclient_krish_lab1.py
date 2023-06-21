# This is tcpclient.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get server's IP address
server = "30.30.30.6"

# set destination port
port = 10000

# connection to hostname on the port.
s.connect((server, port))

#loop infinitely
while True :
    # send message. The string needs to be converted to bytes.
    message = input("Please type your message to the server here ->")
    s.send(message.encode())

    # Close connection when bye message sent
    if message == "bye":
        s.close()
        break

    # Receive no more than 1024 bytes
    msg = s.recv(1024)

    #decode message
    msg_final = msg.decode()

    #print conversation
    print("received: " + msg_final)