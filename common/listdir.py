# *********************************************************************
import os
class ListDirectory:
    def ListDir(self):   
        # define the folder you want to list the files for
        path = '../server'
        dir_list = os.listdir(path)
     
        print("\nCurrent files on the server")
        print("---------------------------")
        for file in dir_list:
            print(file)
        print("\n")