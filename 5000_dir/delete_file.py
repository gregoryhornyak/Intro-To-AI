import os
def DeleteFile(filename):
    filename = filename + "txt"
    os.remove(filename)