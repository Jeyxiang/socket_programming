import time
from socketserver import *
from socketserver import BaseRequestHandler, TCPServer
import socket
import re

def client_bulletin():
    # Input server IP and port
    # host = input("Please enter server IP address: ")
    serverPort = int(input("Please enter server port number: ")) # server port number
    host = socket.gethostname()  # PLACEHOLDER - If both code is running on same pc

    # instantiate the TCP socket for server
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, serverPort))
    print(f"Successfully connected to {host}, port number {serverPort}.")

    # executing commands
    running = True
    while running:
        message = input("Please enter a command: ")  # take input
        print("client: " + message) # Print Client message
        clientSocket.send(message.encode())  # send message to server

        # Client initiates POST command
        if message.strip() == "POST":
            runningPost = True
            print("client: welcome to socket programming")
            while runningPost:
                message1 = input("client: Please enter a POST message: ")
                clientSocket.send(message1.encode())
                if message1 == "#":
                    data = clientSocket.recv(4096).decode() # receive response
                    print(data)
                    extract_data = re.split('server:/*', data)[-1]  # extract message from server
                    if extract_data.lower().strip() == "ok":
                        # Server has acknowledged, close post command
                        print('client: END OF POST MESSAGE')
                        runningPost = False

        # Client initates READ command
        elif message.strip() == "READ":
            # client should wait and listen
            in_read = True
            while in_read:
                data = clientSocket.recv(4096).decode()
                print(data)
                extract_data = re.split('server:/*', data)[-1]
                if extract_data.strip() == '#':
                    print("client: End of READ")
                    in_read = False

        # Client initiates QUIT
        elif message.strip() == 'QUIT':
            data = clientSocket.recv(4096).decode()  # receive response
            print(data)  # show server message
            extract_data = re.split('server:/*', data)[-1]  # extract message from server
            if extract_data.lower().strip() == "ok":
                # Server has acknowledged, close connection
                running = False
                break

        else:
            # Error handling
            data = clientSocket.recv(4096).decode()
            print(data)  # show server message


    print(f'Client closing connection with {host}')
    clientSocket.close()  # close the connection

if __name__ == '__main__':
    client_bulletin()