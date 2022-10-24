import time
from socketserver import *
from socketserver import BaseRequestHandler, TCPServer
import socket
import re

def client_bulletin(host,serverPort):
    host = socket.gethostname()  # as both code is running on same pc
    port = serverPort  # socket server port number
    running = True

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #instantiate the TCP socket for server
    clientSocket.connect((host, serverPort)) #connect to the server

    message = input(" Please enter a message: ")  # take input

    while running:
        print("client: " + message) # client message
        clientSocket.send(message.encode())  # send message to server
        if message.lower().strip() == "post":
            runningPost = True
            newString = "POST\n"
            while runningPost:
                message1 = input("Please enter a POST message: ")
                newString += message1 + "\n"
                print(newString)
                if message1 == "#":
                    print('break POST while loop')
                    runningPost = False

            clientSocket.send(newString.encode())
            #print("reached")
        data = clientSocket.recv(4096).decode()  # receive response

        print(data)  # show in terminal
        extract_data = re.split('server:/*', data)[-1]

        if message.lower().strip() == 'quit':
            if extract_data.lower().strip() == "ok":
                # Server has acknowledged, close connection
                running = False
                break
        message = input("Please enter a message: ")  # again take input
        print("yo")

    print('While loop ended!')
    clientSocket.close()  # close the connection

if __name__ == '__main__':
    #portNo = input("Please enter port number: ")
    client_bulletin("144.214.115.164",1200)