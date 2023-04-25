class PutFile:
    def __init__(self, path, data, size):
        self.path = path
        self.data = data
        self.size = size

    def send_file(self, client_socket):
        bytes_sent = 0

        while bytes_sent != len(self.data):
            bytes_sent += client_socket.send(self.data[bytes_sent:])