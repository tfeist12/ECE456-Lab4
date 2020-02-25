# ECE456-Lab4
Fourth Programming assignment for ECE Computer Networks at Colorado State University
https://colostate.instructure.com/courses/100482/assignments/1085454


Tyler Feist
Lab #4
ECE 456

UDP Socket Program using Python and Geni
Instructions:

Prerequisites:
1) server.py and client.py use the same key variable for encryption/decryption

Server:
1) navigate to the directory with server.py in it via the command line on the server geni node
2) ensure the directory also contains helper.py and L1.py
3) server.py requires 1 command line argument: serverPort
4) run "python3 sender.py <serverPort>"
5) the script will wait to receive a client message, decrypt and display the message, then sends a response message back with the 5 previous messages received.
6) the script ends after it receives 5 client messages

Client:
1) navigate to the directory with client.py in it via the command line on the client geni node
2) ensure the directory also contains helper.py, L1.py, and a file containing the message to be sent
3) client.py requires 3 command line arguments: serverIP, serverPort, and messageFileName
4) run "python3 client.py <serverIP> <serverPort> <messageFileName>"
5) the script will read data from <messageFileName>, encrypt it then send it to the server
6) the server will then return the last five messages received from clients as well as the time and IP
