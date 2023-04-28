# CPSC471
Group project 1

Members: <br />
Eulices Martinez De La Cruz - emartinezdelacruz@csu.fullerton.edu <br />
Lea Albano - Leaalbano@csu.fullerton.edu <br />
Kevin Le - Kevin.lelele@csu.fullerton.edu <br />
Aidan Sunahara - Aidansunahara@csu.fullerton.edu <br />

language - Python

How to execute your program: <br />
1. On a new terminal, navigate to `CPSC471/server` directory <br />
1. Use the command `python server.py 8000` <br />
1. On a new terminal, navigate to `CPSC471/client` directory <br />
4. Use the command `python client.py 127.0.0.1 8000` <br />
1. On the client terminal, the prompt `ftp>` should pop up <br />
1. To use the get command, you have to input `get file.txt` <br />
1. To use the put command, you have to input `put file333.txt` <br />
1. To use the LS command, you have to input `ls` which gives you the current files on the server <br />
1. To use the quit command, type `quit` 

## Notes
* Folder structure should be maintained as common folder module is used by both the client and server. <br />
* Client and Server will only transfer files in their immediate directory, or subdirectories(if given proper path ie `put folder/file333.txt`). <br />