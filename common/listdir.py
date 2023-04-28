# *********************************************************************
import os
class ListDirectory:
    def __init__(self, path):
        self.path = path

    def ListOfFiles(self):
        # define the folder you want to list the files for
        dir_list = os.listdir(self.path)
     
        return dir_list