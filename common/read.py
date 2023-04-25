class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_contents = ''

    def read_file(self):
        with open(self.file_name, 'r') as file:
            self.file_contents = file.read()

    def print_file_contents(self):
        print(self.file_contents)