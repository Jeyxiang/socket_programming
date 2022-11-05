# socket_programming
Simple socket programming for computer networks

Client will create a socket, initiate TCP connection with server.

Client will mainly handle 3 commands:

	POST: the program continues to accept the user input until entering a line that consists only of a "#". The message will be actively sent to the server.

	READ: receive all messages from server and print them to the screen. Then, allow the user to input the next command.

	QUIT: when the client has sent the "QUIT" command and received "OK" from the server in response, close the connection socket.

Disclaimer: Base on the server.py provided (unedited), it is not possible to send all message within one string i.e 'POST\nWelcome socket programming\nText#!\nmore text.\n#\n', 
since the server only adds the post_message only when post_msg_str[-1] != "#". As a result, all the message is send to the server after every user input.

To compile the code, use pyinstaller to create an executable file. 

pip install pyInstaller

In the same directory as the BulletinBoardClient.py file, run pyinstaller --onefile BulletinBoardClient.py.

The following files and folder will be created:
dist (directory)
build (directory)
BulletinBoardClient.spec

Under the dist directory, the BulletinBoardClient.exe file will be created. Run the file, input the server's IP address and port number to establish TCP connection with the server.