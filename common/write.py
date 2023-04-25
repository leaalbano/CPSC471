class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, content):
        with open(self.file_name, 'w') as file:
            file.write(content)