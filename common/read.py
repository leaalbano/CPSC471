class read_file:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_obj = open(self.file_name, "r")f