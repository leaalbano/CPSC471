import sys
import argparse
import socket
sys.path.insert(0, "..")

from common import ReceiveFile, FileWriter, FileReader, PutFile, ListDirectory, split_to_file_size_and_payload_helper


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
        parced_header = self.receive_and_parce_header(conn)
        while parced_header[0] != 'HEAD:QUIT':
            if parced_header[0] == 'HEAD:PUT':
                print('PUT Command received')
                filename, size, payload = split_to_file_size_and_payload_helper(parced_header)
                fileReceiveObject = ReceiveFile(int(size), payload)
                fileReceiveObject.receive_file(conn)
                FileWriter(filename).write_to_file(fileReceiveObject.get_data())
            elif parced_header[0] == 'HEAD:GET':
                print('GET Command received')
                fileName = parced_header[1].split(':')
                fileData = FileReader(sys.path[1] + "/" + fileName[1]).read_file()
                put_file = PutFile(fileData, fileName[1])
                put_file.send_file(conn)
            elif parced_header[0] == 'HEAD:LS':
                print('LS Command received')
                files = ListDirectory(sys.path[1])
                put_file = PutFile(files.ListOfFiles(), "none")
                put_file.send_file(conn)


            parced_header = self.receive_and_parce_header(conn)

        conn.close()

    def receive_and_parce_header(self, conn):
        received_header = conn.recv(80)
        return received_header.decode().split('#')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='IP or hostname')
    args = parser.parse_args()
    print(args.port)
    server = Server('localhost', args.port)
    while True:
        server.start()