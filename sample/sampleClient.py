from socket import *

serverName = "ecs.fullerton.edu"
serverPort = 12000
# Create asocket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the serve r
clientSocket.connect((serverName, serverPort))
# A string we want to send to the serve r
data = "Hello world! This is a very long string. "

bytesSent = 0

# Keep sending bytes until al l bytes are sent
while bytesSent != len(data):
    bytesSent += clientSocket.send(data[bytesSent:])
# Close the socket
clientSocket.close()
