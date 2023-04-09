import os
import shutil

def move():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter file to move")
    src_path=os.path.join(path,name)
    name2=input("Enter destination ")
    des_path=os.path.join(path,name2,name)


    shutil.move(src_path,des_path)
