# Python file detection

import os

file_path = "C:/Users/ACER/python/08-file-io/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("THat is a directory")
else:
    print("That location doesn't exist")