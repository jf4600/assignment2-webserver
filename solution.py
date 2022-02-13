# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a server socket

# Fill in start
def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)
    # Fill in end
  while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept()  # Fill in start             #Fill in end

        try:
            message = connectionSocket.recv(4096).decode()  # Fill in start          #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.readlines()  # Fill in start       #Fill in end
            # Send one HTTP header line into socket
            # Fill in start
            connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n").encode()
            connectionSocket.send("\r\n").encode()  # Empty line
            # Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:
            # Send response message for file not found
            # Fill in start
            connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n")
            connectionSocket.send("Content-Type: text/html\r\n")
            connectionSocket.send("\r\n")
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
