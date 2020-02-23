import sys
import socket
import helper
import L1


# Test length of command line args for client
def testArgLength():
    if len(sys.argv) != 4:
        print("Must use 3 command line arguments for client, Exiting!")
        sys.exit()


# Test validity of arguments read in
def testArgs(sIP, sPort, inFile):
    sIP = helper.testIP(sIP)
    sPort = helper.parsePort(sPort)
    file = L1.testFile(inFile)
    data = file.read()
    file.close()
    return [sIP, sPort, data]


# Main method
if __name__ == '__main__':

    # Parse all command line inputs, test them, then read data
    testArgLength()
    sIP, sPort, inFile = str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])
    sIP, sPort, data = testArgs(sIP, sPort, inFile)
    size = L1.testSize(data)
    print("Data: " + str(data)[2:][:len(data)])

    # Pad the data if necessary
    pad = 0
    if size % 2 != 0:
        pad = 1
        data = L1.pad(data)

    # Set key
    key = "1t]*am0t"
    L1.testKey(key)
    print("Key: " + key + "\n")

    # Encrypt data
    eData = helper.cryption(data, key, pad)

    # Use socket programming to send the encrypted data to the server. Wait for the response and display the response.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket object
    # host = socket.gethostname()
    host = str(sIP)
    sock.sendto(eData, (host, sPort))

    # Receive and print last five messages
    print("Server response:")
    for i in range(0, 5):
        rec, address = sock.recvfrom(1024)
        print(str(rec)[2:][:-1])
    sock.close()
