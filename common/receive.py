class ReceiveFile:
    def __init__(self, size, firstChunk):
        self.size = size
        self.data = firstChunk
        self.bytes_received = len(firstChunk)
        print("Received message:", firstChunk)
        print("Current size:", self.bytes_received)
        print("Total size:", self.size)

    def receive_file(self, client_socket):
        while self.bytes_received < self.size:
            buffer = client_socket.recv(80)
            self.data += buffer.decode()
            print("Received message:", buffer.decode())
            print("Current size:", self.bytes_received)
            print("Total size:", self.size)
            self.bytes_received += len(buffer)

    def get_data(self):
        return self.data