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

    # Set key
    key = "1t]*am0t"
    L1.testKey(key)

    # Initial message log
    mLog = []
    for i in range(0, 5):
        # by = bytes(str(i + 1) + ": Empty", 'utf-8')
        by = str(i + 1) + ": Empty"
        mLog.append(by)

    # Server networking
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket object
    sock.bind(("0.0.0.0", port))
    print("Waiting for client messages\n")

    count = 0
    while count < 5:
        # Receive data from client
        data, address = sock.recvfrom(1024)
        print("Number of messages received: " + str(count + 1))
        print("Received message: " + str(data)[2:][:len(data)] + " from " + str(address[0]))

        # Pad the data if necessary
        pad = 0
        if len(data) % 2 != 0:
            pad = 1
            data = L1.pad(data)

        # Decrypt data
        dData = helper.cryption(data, key, pad)
        print("Decrypted message: " + str(dData)[2:][:len(dData)] + "\n")

        # Build response and set it in message log (count: time, message from address)
        log = str(count + 1) + ": " + str(datetime.datetime.now().time())[:8] + ", " + str(data)[2:][:len(data)] + " from " + address[0]
        mLog[count] = log

        # Send last five messages to the client
        for i in range(0, len(mLog)):
            b = bytearray()
            b.extend(map(ord, mLog[i]))
            sock.sendto(b, address)

        count += 1
