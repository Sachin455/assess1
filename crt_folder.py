import os

def createfolder(path):
    name=input("Enter name of folder you want to create")

    os.mkdir(os.path.join(path,name))



