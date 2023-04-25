import socket

def prompt():
    print("ftp>")
    return input()
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print('Connected to {}:{}'.format(self.host, self.port))

    def start(self):
        while True:
            send_message = input('Enter a message to send: ')
            self.socket.sendall(send_message.encode())

            data = self.socket.recv(1024)
            received_message = data.decode()
            print('Received message:', received_message)

            if not received_message:
                break

        self.socket.close()

if __name__ == '__main__':
    client = Client('localhost', 8000)
    client.connect()
    client.start()

