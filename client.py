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

    # Encrypt the data and convert to a bytearray
    chunks = L1.encrypt(data, key)
    bData = []
    for a in range(0, len(chunks)):
        for b in range(0, len(chunks[a])):
            bData.append(ord(chunks[a][b]))
    bData = bytearray(bData)

    # Write encrypted data to a file
    L1.writeData("encryptedData.txt", chunks, pad)


    # Use socket programming to send the encrypted data to the server. Wait for the response and display the response.

    sock = socket.socket()              # Create a socket object
    sock.connect((sIP, sPort))          # connect to server
    sock.sendto(data, (sIP, sPort))     # send data via UDP




