# Student name: Nick Muenchen
# CID: C63495595

import argparse
from socket import *
import os               # To read the last modified time
import datetime
import sys              # In order to terminate the program

# Read in the arguments for the HTTP Client
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('server_host',
                   help='The server you are trying to contact')
parser.add_argument('server_port', type=int,
                   help='The port for the server')
parser.add_argument('filename',
                   help='The name of the file you wish to download')

# Args contains three values
#args.server_host = the server host you entered when running the program
#args.server_port = the port you want to connect to on the server
#args.filename = the name of the requested file
args = parser.parse_args()

print("server_host: " + args.server_host)
print("server_host: " + str(args.server_port))
print("server_host: " + args.filename)

clientSocket = socket(AF_INET, SOCK_STREAM)   #Complete this code
clientSocket.connect((args.server_host, args.server_port))   #Complete this code)
message = "GET /" + args.filename + " HTTP/1.1\r\n\r\n"
clientSocket.send(message.encode());

# Get the status line
result = clientSocket.recv(2048).decode()    #Complete this code
print(result)

# You need to handle two types of responses: 200 OK responses, and 404 Not Found responses
# Check to see which response was returned by the server and handle it appropriately
#Complete this code
if "200 OK" in result:
    fullResult = ""
    while len(result) > 0:
        result = clientSocket.recv(2048).decode()
        fullResult += result
    print(fullResult)
else:
    if "404 Not Found" in result:
        result = clientSocket.recv(2048).decode()
        print(result)


clientSocket.close()
