class ReceiveFile:
    def __init__(self, data, size):
        self.data = data
        self.size = size

    def receive_file(self, client_socke):
        data = self.socket.recv(1024)
        received_message = data.decode()
        print('Received message:', received_message)
        while bytes_received != len(self.data):
            bytes_received += client_socket.recv(self.data[bytes_received:])
            self.socket.recvall(bytes(self.data, "utf-8"))