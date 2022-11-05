import time
from socketserver import *
from socketserver import BaseRequestHandler, TCPServer
import socket
import sys
import re

def connect_server(host, serverPort):  # Function to connect to server
    try:
        print("IP ADDRESS: ",host)
        print("Port number: ",serverPort)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(3)
        clientSocket.connect((host, serverPort))
    except Exception as e:  # handle error occur
        print("Connect status: FAILED")
        clientSocket.close()
        sys.exit()
    else:
        print("Connect status: OK")
        return clientSocket

def rcv_server_command(socket):
    try:
        data = socket.recv(4096).decode()  # receive response
        print(data)
        extract_data = re.split('server:/*', data)[-1]  # extract message from server
        return extract_data
    except Exception as e:
        print(e)
        socket.close()


def client_bulletin(socket):
    clientSocket = socket
    # executing commands
    running = True
    while running:
        message = input("Please enter a command: ")  # take input
        print("client: " + message) # Print Client message
        clientSocket.send(message.encode())  # send message to server

        # Client initiates POST command
        if message.strip() == "POST":
            runningPost = True
            print("client: running POST")
            while runningPost:
                # send message 1 by 1
                message1 = input("client: Please enter a POST message: ")
                clientSocket.send(message1.encode())
                if message1 == "#":
                    extract_data = rcv_server_command(clientSocket)
                    if extract_data.lower().strip() == "ok":
                        # Server has acknowledged, close post command
                        print('client: END OF POST MESSAGE')
                        runningPost = False


        # Client initates READ command
        elif message.strip() == "READ":
            # client should wait and listen
            in_read = True
            while in_read:
                extract_data = rcv_server_command(clientSocket)
                if extract_data.strip() == '#':
                    print("client: End of READ")
                    in_read = False

        # Client initiates QUIT
        elif message.strip() == 'QUIT':
            extract_data = rcv_server_command(clientSocket)
            if extract_data.lower().strip() == "ok":
                # Server has acknowledged, close connection
                running = False
                break

        else:
            # Error handling
            data = clientSocket.recv(4096).decode()
            print(data)  # show server message


    print("Connect status: QUIT")
    clientSocket.close()  # close the connection

if __name__ == '__main__':
    # Input server IP and port
    host = input("Please enter server IP address: ")
    serverPort = int(input("Please enter server port number: "))  # server port number
    socket_client = connect_server(host,serverPort)
    client_bulletin(socket_client)
