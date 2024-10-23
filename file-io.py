import os

file_name = 'files/test.txt'

def file_remove():
    os.remove(file_name)

def file_write(): 
    file = open(file_name, 'a')

    for i in range(1, 5):
        file.write(f'hello world\n')
    file.close()

def file_read():
    file = open(file_name, 'r')
    text = file.read()
    print(text)

file_remove()
file_write()
file_read()