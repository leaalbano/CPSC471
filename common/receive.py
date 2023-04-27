class ReceiveFile:
    def __init__(self, size, firstChunk):
        self.size = size
        self.data = firstChunk
        self.bytes_received = len(firstChunk)

    def receive_file(self, client_socket):
        while self.bytes_received < self.size:
            buffer = client_socket.recv(80)
            self.data += buffer.decode()
            self.bytes_received += len(buffer)

    def get_data(self):
        return self.data