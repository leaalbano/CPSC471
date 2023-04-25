from socket import *
# The port on which to listen
serverPort = 12000
# Create a TCP s ocket
serverSocket = socket(AF_INET ,SOCK_STREAM)
# Bind the s ocke t to the port
serverSocket.bind(("",serverPort))
# Sta rt l i s t ening for incoming connections
serverSocket.listen(1)
print("The server is ready to receive")
# Forever accept incoming connections
data = ""
while 1 :
     # Accept a connection ; get client ’s s ocke t
     connectionSocket , addr = serverSocket.accept()
     # The temporary bufer
     tmpBuff= ""
     while len(data) != 40:
          # Receive whatever the newly connected client has to send
          tmpBuff = connectionSocket.recv(40 - len ( data ))
          # The other side u n expected ly clo s e d i t ’s s ocke t
          if not tmpBuff :
             break
          # Save the data
          data += tmpBuff

     print(data)
# Close the socket
connectionSocket.close()
