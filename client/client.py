import sys
import argparse
import socket
sys.path.insert(0, "..")

from common import FileReader, PutFile
from common import ListDirectory


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.put_file = None

    def connect(self):
        self.socket.connect((self.host, self.port))
        print('Connected to {}:{}'.format(self.host, self.port))

    def start(self):
        command = self.parse_command(self.prompt())
        while command[0] != 'quit':
            if command[0] == 'ls':
                ls_command = ListDirectory()
                ls_command.ListDir()

                self.send_data_as_bytes('HEAD:LS')
                self.receive_data()
            elif command[0] == 'get':
                self.send_data_as_bytes('HEAD:GET')
            elif command[0] == 'put':
                fileData = FileReader(sys.path[1]+"/" + command[1]).read_file()
                put_file = PutFile(fileData, command[1])
                put_file.send_file(self.socket)
            else:
                print('Invalid command')
            command = self.parse_command(self.prompt())

        self.send_data_as_bytes('HEAD:QUIT')
        self.socket.close()

    def receive_data(self):
        data = self.socket.recv(25)
        received_message = data.decode()
        print('Received message:', received_message)
        pass

    def prompt(self):
        return input("ftp> ")

    def parse_command(self, command):
        return command.split(' ')

    def send_data_as_bytes(self, data):
        self.socket.sendall(bytes(data, "utf-8"))


if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('host', type=str, help='IP or hostname')
     parser.add_argument('port', type=int, help='the Port to connect on')
     args = parser.parse_args()
     client = Client(args.host, args.port)
     client.connect()
     client.start()

