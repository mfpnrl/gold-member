#!/usr/bin/env python3.7

import os

# Get the current working directory 
cwd = os.getcwd()
current_dir = os.getcwd()

# Create an empty list to store the file information
file_info = []

# Walk through directory tree and get file information
for dirpath, dirnames, filenames in os.walk(current_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_info.append({"name" : file, "size" : file_size})
        
# Print the list of the file information
for file in file_info:
    print(file)

