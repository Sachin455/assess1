import os
path='/home/vboxuser/Desktop/new-folder/assesment'
def list():
    print("Hello lets start working")
    print(os.getcwd())
    print(os.listdir(path))

list()