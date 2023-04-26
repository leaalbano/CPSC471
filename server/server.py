import sys
import argparse
import socket
sys.path.insert(0, "..")

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
        data = conn.recv(15)
        parced_data = self.parse_command(data.decode())
        while parced_data[0] != 'HEAD:QUIT':

            if not data:
                break
            received_message = data.decode()

            if parced_data[0] == 'HEAD:LS':
                print('LS Command received')
            elif parced_data[0] == 'HEAD:GET':
                print('GET Command received')
            elif parced_data[0] == 'HEAD:PUT':
                print('PUT Command received')


            send_message = 'ok'
            conn.sendall(send_message.encode())
            data = conn.recv(15)
            parced_data = self.parse_command(data.decode())

        conn.close()

    def parse_command(self, command):
        return command.split('#')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='IP or hostname')
    args = parser.parse_args()
    print(args.port)
    server = Server('localhost', args.port)
    while True:
        server.start()