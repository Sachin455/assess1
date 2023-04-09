import os

def hidden_folder():
    path="/home/vboxuser/Desktop"
    name=input("Enter name you want to show")
    name2='.'+name
    path_name=os.path.join(path,name)
    hidden_name=os.path.join(path,name2)

    os.rename(hidden_name,path_name)

hidden_folder()