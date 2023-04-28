import sys
import argparse
import socket
sys.path.insert(0, "..")

from common import FileReader, PutFile, ReceiveFile, FileWriter, ListDirectory


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
        command = self.prompt().split(' ')
        while command[0] != 'quit':
            if command[0] == 'ls':
                self.send_data_as_bytes('HEAD:LS')
                self.receive_dir_data()
            elif command[0].lower() == 'get':
                self.send_data_as_bytes('HEAD:GET#FILE:'+command[1])
                self.receive_file_data()
            elif command[0].lower() == 'put':
                fileData = FileReader(sys.path[1]+"/" + command[1]).read_file()
                put_file = PutFile(fileData, command[1])
                put_file.send_file(self.socket)
            else:
                print('Invalid command')
            command = self.prompt().split(' ')

        self.send_data_as_bytes('HEAD:QUIT')
        self.socket.close()

    def receive_file_data(self):
        data = self.socket.recv(80)
        parced_data = data.decode().split('#')
        fileName = parced_data[1].split(':')
        size = parced_data[2].split(':')
        payload = parced_data[3].split(':')
        fileReceiveObject = ReceiveFile(int(size[1]), payload[1])
        fileReceiveObject.receive_file(self.socket)
        dataToWrite = fileReceiveObject.get_data()
        FileWriter(fileName[1]).write_to_file(dataToWrite)

    def receive_dir_data(self):
        data = self.socket.recv(80)
        parced_data = data.decode().split('#')
        size = parced_data[2].split(':')
        payload = parced_data[3].split(':')
        fileReceiveObject = ReceiveFile(int(size[1]), payload[1])
        fileReceiveObject.receive_file(self.socket)
        dataToWrite = fileReceiveObject.get_data()
        print(dataToWrite)

    def receive_directory_data(self):
        pass

    def prompt(self):
        return input("ftp> ")

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

