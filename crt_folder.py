import os

def createfolder(path):
   # path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter name of folder you want to create")

    os.mkdir(os.path.join(path,name))



