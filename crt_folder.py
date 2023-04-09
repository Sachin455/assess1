import os

def createfolder():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter name of folder you want to create")
    new_path=os.path.join(path,name)

    os.mkdir(new_path)

createfolder()

