import time
from socketserver import *
from socketserver import BaseRequestHandler, TCPServer
import socket
import re

def client_bulletin(host,serverPort):
    host = socket.gethostname()  # If both code is running on same pc
    port = serverPort  # socket server port number
    running = True

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #instantiate the TCP socket for server
    clientSocket.connect((host, serverPort)) #connect to the server

    message = input(" Please enter a message: ")  # take input

    while running:
        print("client: " + message) # Print Client message
        clientSocket.send(message.encode())  # send message to server

        if message.lower().strip() == "post":
            runningPost = True
            while runningPost:
                message1 = input("Please enter a POST message: ")
                clientSocket.send(message1.encode())
                if message1 == "#":
                    print('break POST while loop')
                    # Server should be acknowledge with OK
                    runningPost = False


        data = clientSocket.recv(4096).decode()  # receive response

        print(data)  # show server message
        extract_data = re.split('server:/*', data)[-1] # extract message from server

        # Client initiates QUIT
        if message.lower().strip() == 'quit':
            if extract_data.lower().strip() == "ok":
                # Server has acknowledged, close connection
                running = False
                break
        message = input("Please enter a message: ")  # again take input

    print('Client closing connection')
    clientSocket.close()  # close the connection

if __name__ == '__main__':
    #ipAddress = input("Please enter host address: ")
    portNo = 1200
    client_bulletin("placeHolder",portNo)