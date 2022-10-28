# socket_programming
simple socket programming for computer networks


Client will create a socket, initiate TCP connection with server.

Client will mainly handle 3 commands:
POST: the program continues to accept the user input until entering a line that consists only of a "#" followed by a newline character '\n'. Then, send this command and these messages to the server.
READ: receive all messages from server and print them to the screen. Then, allow the user to input the next command.
QUIT: when the client has sent the "QUIT" command and received "OK" from the server in response, close the connection socket.
