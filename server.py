import sys
import socket
import datetime
import helper
import L1


# Test length of command line args for client
def testArgLength():
    if len(sys.argv) != 2:
        print("Must use 1 command line argument for server, Exiting!")
        sys.exit()


# Test validity of arguments read in
def testArgs(port):

    port = helper.parsePort(port)
    return port

# Main method
if __name__ == '__main__':

    # Parse all command line inputs, test them, then read data
    testArgLength()
    port = str(sys.argv[1])
    port = testArgs(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket object
    sock.bind(('', port))
    print("Waiting for client messages")

    count = 0
    while count < 5:
        data, address = sock.recvfrom(1024)
        print("Received message: " + str(data)[2:][:len(data)] + " from " + str(address[0]))
        sock.sendto(b'Received: ' + data, address)
        count += 1