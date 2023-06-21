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

