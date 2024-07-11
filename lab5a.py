#!/usr/bin/env python3
# Author ID: ateimouri1

def read_file_string(file_name):
    f = open(file_name, 'r') #open the ile with read mode
    content = f.read() #read the full content of the file
    f.close() #close the file
    return content #return the content

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = [line.strip() for line in f] #read each line of the file
    f.close()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))  #print the content of the file as a single string
    print(read_file_list(file_name)) #print the content of the file as a list of lines