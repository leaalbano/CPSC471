import argparse
import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

    def start(self):
        self.socket.listen()
        print('Server listening on {}:{}'.format(self.host, self.port))
        conn, addr = self.socket.accept()
        print('Connected by', addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            received_message = data.decode()
            print('Received message:', received_message)

            send_message = input('Enter a message to send: ')
            conn.sendall(send_message.encode())

        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='IP or hostname')
    args = parser.parse_args()
    print(args.port)
    server = Server('localhost', args.port)
    server.start()