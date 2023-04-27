# *********************************************************************
import os
class ListDirectory:
    def ListDir(self):   

        # define the folder you want to list the files for
        path = '../client/test'
        dir_list = os.listdir(path)
        print("Files and directories in '", path, "' :")
        print(dir_list)
