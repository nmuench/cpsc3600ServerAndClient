# Student name: Nick Muenchen
# CID: C63495595

#import socket module
from socket import *
import os               # To read the last modified time
import datetime         # To format the last modified time
import sys              # In order to terminate the program

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)      #Complete this code

#Prepare a sever socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Complete this code

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()   #Complete this code
    try:
        message = connectionSocket.recv(2048).decode() #Complete this code
        # Find the filename of the requested file
        filename = message.split()[1]

        # Open and read the file
        f = open(filename[1:])
        outputdata = f.read()

        # Find the date the file was last modified
        statbuf = os.stat(filename[1:])
        last_modified = datetime.datetime.fromtimestamp(
            int(statbuf.st_mtime)
        ).strftime("Last-Modified: %a, %d %b %Y %H:%M:%S %Z\r\n")  #Complete this code

        #Send one HTTP header line into socket
        headerText = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(headerText.encode())        # Complete this code
        headerText = last_modified
        connectionSocket.send(headerText.encode())
        headerText = "\r\n"
        connectionSocket.send(headerText.encode())


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        # Close client socket
        #Complete this code
    except IOError:
        sendText = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(sendText.encode())
        #Send response message for file not found
        #Complete this code

        #Close client socket
        connectionSocket.close()    #Complete this code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
