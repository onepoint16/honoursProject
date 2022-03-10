import os

def get_file_name(file_dir):
    files = os.listdir(file_dir) 
    s = ""
    for file in files: 
        str_name = file[:29]
        s = str_name
    return s

def get_file_names(file_dir):
    files = os.listdir(file_dir) 
    s = []
    for file in files: 
        str_name = file[:29]
        s.append(str_name) 
    return s