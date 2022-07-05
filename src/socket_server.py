#! /usr/bin/python
#---------------------------------------------

from socket import *

server= socket(AF_PACKET,SOCK_RAW)

host='eth0'
port=4096

address=(host,port)
server.bind(address)

print("started listening " + host + ": " ,port)
client,addr=server.accept()
print("Got a connection from " + addr[0], ": ",addr[1])
while True:
    data =client.recv(4096)
    print("Received" + data + " from the client" )
    print ("proccesing data")
    if(data == "Hello server"):
        client.send(("Hello client").encode('utf-8'))
        print("  Proccesing done. \n   Reply Send")
    elif(data =="disconnect"):
        client.send(("Goodbye").encode('utf-8'))
        client.close()
        break
    else:
        client.send((" Invalid data ").encode('utf-8'))
        print("  Proccessing done Invalid data . \n Reply send ")
