# ********************** SERVER HALF OF THE CODE ************************

# This is tcpserver.py file
import socket                                         

# create a TCP/IP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# update with the IP address of your local machine
host = "30.30.30.6"                         

#set port number for this server
port = 10000                                          

# bind to the port
serversocket.bind((host, port))                                  

# Listen for incoming connections, queue up to 5 requests
serversocket.listen(5)                                           

# wait for a connection
print('waiting for a connetion on port ' + str(port) + '\n')
clientsocket,addr = serversocket.accept()      

print("Got a connection from " + str(addr))

while True:
   # Receive the data of 1024 bytes maximum. The received data is binary data. 
   data = clientsocket.recv(1024)
   print("received: " + data.decode())

   if data.decode() == "bye":
      clientsocket.close()
      break

   #Send a reply to client
   msg = input("Please a type a reply to client->")
   clientsocket.send(msg.encode())

# ********************* CLIENT HALF OF THE CODE *************************

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