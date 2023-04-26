class PutFile:
    def __init__(self, data, fileName):
        self.data = data
        self.fileName = fileName

    def send_file(self, client_socket):
        bytes_sent = 0

        payload = self.build_message()

        while bytes_sent != len(payload):
            bytes_sent += client_socket.send(bytes(payload[bytes_sent:], "utf-8"))

    def build_message(self):
        size = len(self.data)
        headerMessage = "HEAD:PUT#FILE:" + self.fileName  + "#SIZE:"+ str(size)+"#PAYLOAD:"
        return headerMessage + str(self.data)