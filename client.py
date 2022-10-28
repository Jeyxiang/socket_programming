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
    print(f"Connected to {host}")
    #message = input(" Please enter a message: ")  # take input

    while running:
        message = input("Please enter a message: ")  # again take input
        print("client: " + message) # Print Client message
        clientSocket.send(message.encode())  # send message to server

        # Client initiates POST command
        if message.lower().strip() == "post":
            runningPost = True
            while runningPost:
                message1 = input("client: Please enter a POST message: ")
                clientSocket.send(message1.encode())
                if message1 == "#":
                    # Server should be acknowledge with OK
                    data = clientSocket.recv(4096).decode()
                    print(data)
                    extract_data = re.split('server:/*', data)[-1]  # extract message from server
                    if extract_data.lower().strip() == "ok":
                        # Server has acknowledged, close post command
                        print('client: END OF POST MESSAGE')
                        runningPost = False

        # Client initates READ command
        elif message.lower().strip() == "read":
            # client should wait and listen
            in_read = True
            while in_read:
                data = clientSocket.recv(4096).decode()
                print(data)
                extract_data = re.split('server:/*', data)[-1]  # extract message from server
                if extract_data.strip() == '#':
                    print("client: End of READ")
                    in_read = False # end reading

        # Client initiates QUIT
        elif message.lower().strip() == 'quit':
            data = clientSocket.recv(4096).decode()  # receive response
            print(data)  # show server message
            extract_data = re.split('server:/*', data)[-1]  # extract message from server
            if extract_data.lower().strip() == "ok":
                # Server has acknowledged, close connection
                running = False
                break

        else:
            data = clientSocket.recv(4096).decode()  # receive response
            print(data)  # show server message


    print(f'Client closing connection with {host}')
    clientSocket.close()  # close the connection

if __name__ == '__main__':
    #ipAddress = input("Please enter host address: ")
    portNo = 1200
    client_bulletin("placeHolder",portNo)