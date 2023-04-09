import os

def hide_folder():
    path="/home/vboxuser/Desktop"
    name=input("Enter name you want to hide")
    name2='.'+name
    path_name=os.path.join(path,name)
    hide_name=os.path.join(path,name2)

    os.rename(path_name,hide_name)

hide_folder()

