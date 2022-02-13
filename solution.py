# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)

    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        #print(f"Connection from {addr} has been established!")
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        # Fill in start      #Fill in end
        try:

            try:
                connectionSocket, addr = serverSocket.accept()
                message = serverSocket.recv(1024)
                #print(message.decode("utf-8"))
                # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                # Fill in start     #Fill in end

                # Send one HTTP header line into socket.
                connectionSocket.send("HTTP/1.1 200\r\n".encode)
                # Fill in start

                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode)
                # Fill in start
                connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>")
                # Fill in end

                # Close client socket
                connectionSocket.close()
                # Fill in start

                # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

